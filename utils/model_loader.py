import pickle
import os
import logging
import sys

def load_model_and_scaler():
    """
    Load the trained phishing detection model with absolute path
    """
    try:
        # Get the absolute path - In Docker, it's usually /app
        base_dir = '/app'  # Docker container working directory
        model_path = os.path.join(base_dir, 'phishing_model.pkl')
        scaler_path = os.path.join(base_dir, 'scaler.pkl')
        
        # Print debug info (will show in Render logs)
        print(f"=== MODEL LOADING DEBUG ===")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Base directory: {base_dir}")
        print(f"Model path: {model_path}")
        print(f"Files in /app: {os.listdir('/app') if os.path.exists('/app') else 'Not found'}")
        
        # Check if model file exists
        if not os.path.exists(model_path):
            # Try alternative paths
            alt_paths = [
                './phishing_model.pkl',
                '../phishing_model.pkl',
                'phishing_model.pkl',
                '/app/phishing_model.pkl'
            ]
            
            for alt_path in alt_paths:
                if os.path.exists(alt_path):
                    model_path = alt_path
                    print(f"Found model at: {model_path}")
                    break
            else:
                # List all files to help debug
                all_files = []
                for root, dirs, files in os.walk('/app'):
                    for file in files:
                        if file.endswith('.pkl'):
                            all_files.append(os.path.join(root, file))
                print(f"All .pkl files found: {all_files}")
                
                raise FileNotFoundError(f"Model file not found. Tried: {model_path} and {alt_paths}")
        
        # Check file size
        file_size = os.path.getsize(model_path)
        print(f"Model file size: {file_size} bytes")
        
        if file_size == 0:
            raise ValueError(f"Model file is empty: {model_path}")
        
        # Load model
        print(f"Loading model from {model_path}")
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        
        print(f"Model loaded successfully. Type: {type(model).__name__}")
        
        # Try to load scaler
        if os.path.exists(scaler_path) and os.path.getsize(scaler_path) > 0:
            print(f"Loading scaler from {scaler_path}")
            with open(scaler_path, 'rb') as scaler_file:
                scaler = pickle.load(scaler_file)
            print("Scaler loaded successfully")
        else:
            # Create a dummy scaler
            scaler = DummyScaler()
            print("Scaler file not found. Using DummyScaler")
        
        print("=== MODEL LOADING COMPLETE ===")
        return model, scaler
    
    except Exception as e:
        print(f"ERROR loading model: {str(e)}")
        logging.error(f"Error loading model/scaler: {str(e)}")
        raise

class DummyScaler:
    """A dummy scaler that returns the input unchanged"""
    def __init__(self):
        self.mean_ = None
        self.scale_ = None
    
    def transform(self, X):
        return X
    
    def fit_transform(self, X):
        return X
    
    def fit(self, X):
        return self
    
    def inverse_transform(self, X):
        return X
