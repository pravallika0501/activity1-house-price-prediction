# House Price Prediction

This project predicts house prices based on features such as the number of bedrooms, bathrooms, square footage, and more. It uses Python, scikit-learn for machine learning, and Flask for a simple web interface where users can input house features and get predicted prices.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [How to Run](#how-to-run)
- [Model Training](#model-training)
- [License](#license)

## Project Structure

```bash
house-price-prediction/
│
├── data/                        # Stores the dataset
│   └── data.csv                 # Dataset file
│
├── src/                         # Source code
│   ├── data_processing.py       # Data cleaning and preprocessing
│   ├── model.py                 # Model training and evaluation
│   ├── predict.py               # Prediction functionality
│
├── app/                         # Flask web app
│   ├── templates/               # HTML templates for the web app
│   │   └── index.html           # Web page for user input
│   ├── app.py                   # Flask application code
│   └── model.pkl                # Serialized model (after training)
│
├── models/                      # Folder to store trained models
│   └── linear_regression_model.pkl
│
├── README.md                    # Project description
└── requirements.txt             # Python dependencies
