import joblib
import pandas as pd
import sys
import os

# Add the parent directory of `app` to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.predict import load_model, make_prediction


def load_model(filepath):
    """Loads the trained model from a file."""
    return joblib.load(filepath)

def make_prediction(model, input_data):
    """Makes a prediction based on the input data."""
    df = pd.DataFrame(input_data, index=[0])
    prediction = model.predict(df)
    return prediction[0]
