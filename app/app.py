from flask import Flask, render_template, request
import pandas as pd
import sys
import os
# Add the parent directory of `app` to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.predict import load_model, make_prediction




app = Flask(__name__)

# Load the pre-trained model
model = load_model('model.pkl')

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle form submission for house price prediction."""
    # Get form inputs
    input_data = {
        'bedrooms': int(request.form['bedrooms']),
        'bathrooms': int(request.form['bathrooms']),
        'sqft_living': int(request.form['sqft_living']),
        'sqft_lot': int(request.form['sqft_lot']),
        'floors': int(request.form['floors']),
        'view': int(request.form['view']),
        'condition': int(request.form['condition'])
    }

    # Make prediction using the trained model
    prediction = make_prediction(model, input_data)
    
    return render_template('index.html', prediction_text=f'Predicted House Price: ${prediction:,.2f}')

if __name__ == '__main__':
    app.run(debug=True)
