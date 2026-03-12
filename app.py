import os
import logging
from flask import Flask, render_template, request, jsonify, session
from utils.model_loader import load_model_and_scaler, DummyScaler
from utils.feature_extractor import extract_features, get_feature_names
import numpy as np
from datetime import timedelta
import secrets
import traceback

# Configure logging
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.permanent_session_lifetime = timedelta(minutes=30)

# Load model and scaler at startup
try:
    MODEL, SCALER = load_model_and_scaler()
    logging.info("Application started successfully")
    
    # Verify feature count
    if hasattr(MODEL, 'n_features_in_'):
        expected_features = MODEL.n_features_in_
        logging.info(f"Model expects {expected_features} features")
        if expected_features != 23:
            logging.warning(f"Model expects {expected_features} features, but code uses 23")
    else:
        logging.info("Model doesn't expose n_features_in_, assuming it expects 23 features")
    
except Exception as e:
    logging.error(f"Failed to load model: {str(e)}")
    logging.error(traceback.format_exc())
    MODEL = None
    SCALER = None

@app.route('/')
def index():
    """Home page"""
    if MODEL is None:
        return render_template('error.html', 
                             error="Model not loaded. Please check the logs.",
                             details="The machine learning model could not be loaded.")
    return render_template('index.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Predict if a URL is phishing or legitimate"""
    try:
        # Check if model is loaded
        if MODEL is None:
            return render_template('result.html', 
                                 error="System is not ready. Please try again later.",
                                 url=request.form.get('url', ''))
        
        # Get URL from form
        url = request.form.get('url', '').strip()
        
        if not url:
            return render_template('result.html', 
                                 error="Please enter a URL",
                                 url=url)
        
        # Add http:// if missing
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        # Log the prediction request
        logging.info(f"Predicting URL: {url}")
        
        # Extract features from URL
        features = extract_features(url)
        
        # Get feature names in correct order
        feature_names = get_feature_names()
        
        # Create feature array in correct order
        feature_values = [features.get(name, 0) for name in feature_names]
        feature_array = np.array([feature_values])
        
        logging.info(f"Feature array shape: {feature_array.shape}")
        logging.info(f"First 5 feature values: {feature_values[:5]}")
        
        # Scale features (if scaler is available, otherwise use as is)
        if SCALER is not None and not isinstance(SCALER, DummyScaler):
            features_scaled = SCALER.transform(feature_array)
        else:
            features_scaled = feature_array
        
        # Make prediction
        if hasattr(MODEL, 'predict_proba'):
            prediction = MODEL.predict(features_scaled)[0]
            probabilities = MODEL.predict_proba(features_scaled)[0]
            
            if prediction == 1:
                confidence = float(probabilities[1] * 100)
            else:
                confidence = float(probabilities[0] * 100)
        else:
            # For models without predict_proba
            prediction = MODEL.predict(features_scaled)[0]
            confidence = 95.0  # Default confidence
        
        # Interpret result
        if prediction == 1:
            result = "phishing"
            message = "⚠️ WARNING: This URL appears to be a PHISHING website!"
            alert_class = "alert-danger"
            icon = "fa-exclamation-triangle"
        else:
            result = "legitimate"
            message = "✅ SAFE: This URL appears to be LEGITIMATE"
            alert_class = "alert-success"
            icon = "fa-check-circle"
        
        # Log prediction result
        logging.info(f"Prediction for {url}: {result} (confidence: {confidence:.2f}%)")
        
        # Store in session for history
        if 'history' not in session:
            session['history'] = []
        
        session['history'].append({
            'url': url[:50] + '...' if len(url) > 50 else url,
            'result': result,
            'confidence': f"{confidence:.2f}%"
        })
        session.modified = True
        
        return render_template('result.html',
                             url=url,
                             result=result,
                             confidence=f"{confidence:.2f}",
                             message=message,
                             alert_class=alert_class,
                             icon=icon,
                             features=features)
    
    except Exception as e:
        logging.error(f"Error predicting URL: {str(e)}")
        logging.error(traceback.format_exc())
        return render_template('result.html',
                             error=f"An error occurred: {str(e)}",
                             url=url if 'url' in locals() else '')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for predictions"""
    try:
        if MODEL is None:
            return jsonify({'error': 'Model not loaded'}), 503
        
        data = request.get_json()
        url = data.get('url', '').strip()
        
        if not url:
            return jsonify({'error': 'No URL provided'}), 400
        
        # Add http:// if missing
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        # Extract features
        features = extract_features(url)
        feature_names = get_feature_names()
        feature_values = [features.get(name, 0) for name in feature_names]
        feature_array = np.array([feature_values])
        
        if SCALER is not None and not isinstance(SCALER, DummyScaler):
            features_scaled = SCALER.transform(feature_array)
        else:
            features_scaled = feature_array
            
        prediction = MODEL.predict(features_scaled)[0]
        
        if hasattr(MODEL, 'predict_proba'):
            probabilities = MODEL.predict_proba(features_scaled)[0]
            confidence = float(probabilities[1] if prediction == 1 else probabilities[0])
        else:
            confidence = 0.95
        
        return jsonify({
            'success': True,
            'url': url,
            'prediction': 'phishing' if prediction == 1 else 'legitimate',
            'confidence': confidence,
            'features': {name: features.get(name, 0) for name in feature_names[:10]}  # Return first 10 features
        })
    
    except Exception as e:
        logging.error(f"API error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/history')
def history():
    """View prediction history"""
    history_list = session.get('history', [])
    return render_template('history.html', history=history_list)

@app.route('/clear-history', methods=['POST'])
def clear_history():
    """Clear prediction history"""
    session.pop('history', None)
    return jsonify({'success': True})

@app.route('/health')
def health():
    """Health check endpoint"""
    if MODEL is None:
        return jsonify({'status': 'degraded', 'message': 'Model not loaded'}), 503
    
    expected_features = MODEL.n_features_in_ if hasattr(MODEL, 'n_features_in_') else 'unknown'
    
    return jsonify({
        'status': 'healthy',
        'model_loaded': True,
        'model_type': type(MODEL).__name__,
        'scaler_loaded': SCALER is not None and not isinstance(SCALER, DummyScaler),
        'expected_features': expected_features,
        'features_provided': 23
    })

@app.route('/debug/features')
def debug_features():
    """Debug endpoint to check feature extraction"""
    url = request.args.get('url', 'https://example.com')
    
    # Add http:// if missing
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    features = extract_features(url)
    feature_names = get_feature_names()
    feature_values = [features.get(name, 0) for name in feature_names]
    
    return jsonify({
        'url': url,
        'features': features,
        'feature_count': len(features),
        'feature_names': feature_names,
        'feature_values': feature_values,
        'feature_values_preview': feature_values[:5]
    })

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    logging.error(f"Server Error: {error}")
    return render_template('500.html'), 500
@app.route('/debug/paths')
def debug_paths():
    """Debug endpoint to check file paths"""
    import os
    import sys
    
    result = {
        'current_working_dir': os.getcwd(),
        'python_path': sys.path,
        'files_in_current_dir': os.listdir('.'),
        'files_in_root': os.listdir('/') if os.path.exists('/') else [],
        'model_exists': os.path.exists('phishing_model.pkl'),
        'model_absolute_path': os.path.abspath('phishing_model.pkl') if os.path.exists('phishing_model.pkl') else 'Not found',
        'model_size': os.path.getsize('phishing_model.pkl') if os.path.exists('phishing_model.pkl') else 0,
        'utils_exists': os.path.exists('utils'),
        'utils_files': os.listdir('utils') if os.path.exists('utils') else [],
    }
    return jsonify(result)
if __name__ == '__main__':
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    print("=" * 50)
    print("Phishing URL Detection System")
    print("=" * 50)
    print(f"Model loaded: {MODEL is not None}")
    if MODEL is not None:
        if hasattr(MODEL, 'n_features_in_'):
            print(f"Model expects: {MODEL.n_features_in_} features")
            print(f"Code provides: 23 features")
            if MODEL.n_features_in_ != 23:
                print("⚠️  WARNING: Feature count mismatch!")
        else:
            print(f"Model type: {type(MODEL).__name__}")
            print("Code provides: 23 features")
    print(f"Scaler loaded: {SCALER is not None and not isinstance(SCALER, DummyScaler)}")
    print("-" * 50)
    print("Access the application at http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
