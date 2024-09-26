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

## Installation

To set up and run the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/house-price-prediction.git
   cd house-price-prediction
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   - On macOS and Linux:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
## Usage

This project includes both model training and a web application for making predictions.

1. **Train the Model**:

   If the model is not trained yet, run the training script to train the model and save it as `model.pkl`.

   - Open the `src/model.py` file and run the model training code.
   - Save the trained model to the `app/` folder as `model.pkl`.

2. **Run the Flask App**:

   Once the model is trained and saved as `model.pkl`, you can run the Flask web application by running:

   ```bash
   python app/app.py
   ```

3. **Access the Web App**:

   Open your browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

   Enter the house features (bedrooms, bathrooms, square footage, etc.) into the form, and the app will display a predicted house price.

## Model Training

Follow these steps to train the model:

1. **Prepare the Dataset**:

   Ensure the dataset is placed in the `data/` folder and named `data.csv`. The dataset should contain relevant features like bedrooms, bathrooms, square footage, etc.

2. **Train the Model**:

   - Open the `src/model.py` file.
   - Use the code provided in the `train_model` function to train a linear regression model or modify it to train other models.
   - Once the model is trained, it will be saved in the `app/` folder as `model.pkl` using the `save_model()` function.

   Example:

   ```python
   # Example: training the model and saving it
   from src.model import train_model, save_model
   from src.data_processing import load_data, clean_data, preprocess_data

   # Load and preprocess data
   data = load_data('data/data.csv')
   clean_data = clean_data(data)
   X_train, X_test, y_train, y_test = preprocess_data(clean_data)

   # Train and save the model
   model = train_model(X_train, y_train)
   save_model(model, 'app/model.pkl')
   ```

3. **Verify the Model**:

   After training, you can evaluate the model performance using the `evaluate_model` function in `src/model.py`. It calculates metrics like Mean Squared Error (MSE) and R-squared score.

   ```python
   from src.model import evaluate_model

   mse, r2 = evaluate_model(model, X_test, y_test)
   print(ff"Model Performance: MSE = {mse}, R-squared = {r2}")
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

