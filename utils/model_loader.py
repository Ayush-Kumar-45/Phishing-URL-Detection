# utils/model_loader.py
import pickle
import os
import logging
import numpy as np

def load_model_and_scaler():
    """
    Load the trained phishing detection model
    If scaler is not available, create a dummy scaler that returns features unchanged
    """
    try:
        # Get the absolute path to the project root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(base_dir, 'phishing_model.pkl')
        scaler_path = os.path.join(base_dir, 'scaler.pkl')
        
        # Check if model file exists
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        
        # Check file size
        if os.path.getsize(model_path) == 0:
            raise ValueError(f"Model file is empty: {model_path}")
        
        # Load model
        logging.info(f"Loading model from {model_path}")
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        
        logging.info(f"Model loaded successfully. Type: {type(model).__name__}")
        
        # Try to load scaler, if not available create a dummy scaler
        if os.path.exists(scaler_path) and os.path.getsize(scaler_path) > 0:
            logging.info(f"Loading scaler from {scaler_path}")
            with open(scaler_path, 'rb') as scaler_file:
                scaler = pickle.load(scaler_file)
            logging.info("Scaler loaded successfully")
        else:
            # Create a dummy scaler that returns the input unchanged
            scaler = DummyScaler()
            logging.warning("Scaler file not found or empty. Using DummyScaler (no scaling applied)")
        
        return model, scaler
    
    except Exception as e:
        logging.error(f"Error loading model/scaler: {str(e)}")
        raise

class DummyScaler:
    """
    A dummy scaler that returns the input unchanged
    This is used when the original scaler file is not available
    """
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

def get_model_info():
    """Get information about the loaded model"""
    try:
        model, scaler = load_model_and_scaler()
        
        info = {
            'model_type': type(model).__name__,
            'scaler_type': type(scaler).__name__,
        }
        
        # Try to get model parameters if available
        if hasattr(model, 'get_params'):
            info['model_params'] = model.get_params()
        
        # Get feature count if available
        if hasattr(model, 'n_features_in_'):
            info['n_features_in'] = model.n_features_in_
        elif hasattr(model, 'n_features_'):
            info['n_features_in'] = model.n_features_
        else:
            info['n_features_in'] = 'unknown'
        
        return info
    except Exception as e:
        logging.error(f"Error getting model info: {str(e)}")
        return {'error': str(e)}