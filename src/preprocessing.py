# src/preprocessing.py
import pandas as pd
from mongodb_connector import connect_to_mongodb, fetch_data

def load_data_from_mongodb(uri, db_name, collection_name):
    """Load data from a MongoDB collection into a Pandas DataFrame."""
    db = connect_to_mongodb(uri, db_name)
    collection = db[collection_name]
    data = fetch_data(collection)
    return pd.DataFrame(data)

def clean_data(df):
    """Clean data by handling missing values and outliers."""
    df.fillna(df.mean(), inplace=True)  # Handle missing values
    # Add outlier treatment here
    return df
