



## 4) `src` scripts — copy each of the following into files under `classification-project/src/`

### `preprocessing.py`
python
"""preprocessing.py
Utilities for loading, cleaning, encoding, and scaling data for classification tasks.
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def load_data(path):
    """Load CSV data into a DataFrame."""
    return pd.read_csv(path)

def basic_clean(df):
    """Simple cleaning: drop duplicates; extend with your own rules."""
    df = df.copy()
    df = df.drop_duplicates()
    return df

def preprocess_features(df, target_col=None, scale=True):
    """
    Preprocess features:
    - Impute missing values for numeric and categorical
    - One-hot encode categorical variables
    - Optionally scale numeric features
    Returns: X, y (y is None if target_col is None)
    """
    df = df.copy()
    if target_col is not None:
        y = df[target_col].copy()
        X = df.drop(columns=[target_col])
    else:
        y = None
        X = df
    # Numeric and categorical columns
    num_cols = X.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()

    if num_cols:
        num_imputer = SimpleImputer(strategy='median')
        X[num_cols] = num_imputer.fit_transform(X[num_cols])
    if cat_cols:
        cat_imputer = SimpleImputer(strategy='most_frequent')
        X[cat_cols] = cat_imputer.fit_transform(X[cat_cols])

    # One-hot encode categorical variables (simple)
    if cat_cols:
        X = pd.get_dummies(X, columns=cat_cols, drop_first=True)

    if scale and num_cols:
        scaler = StandardScaler()
        X[num_cols] = scaler.fit_transform(X[num_cols])
        joblib.dump(scaler, BASE / 'outputs' / 'model_artifacts' / 'scaler.pkl')

    return X, y

def make_train_test(df, target_col, test_size=0.2, random_state=42):
    X, y = preprocess_features(df, target_col)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    print('This module provides preprocessing helpers. Import functions in your pipeline.')
