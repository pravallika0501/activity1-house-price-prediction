import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    """Loads the dataset from a CSV file."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Performs basic data cleaning."""
    df['date'] = pd.to_datetime(df['date'])  # Convert date to datetime
    df.drop_duplicates(inplace=True)  # Remove duplicates
    df.dropna(inplace=True)  # Drop missing values (customize as needed)
    return df

def preprocess_data(df):
    """Preprocess the data by scaling numeric features."""
    features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'view', 'condition']
    X = df[features]
    y = df['price']

    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test
