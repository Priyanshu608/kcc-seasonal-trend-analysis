import pandas as pd
import numpy as np
from pathlib import Path

def load_dataset(file_path: str) -> pd.DataFrame:
    """Load raw dataset from the given path."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found at: {file_path}")
    return pd.read_csv(path)

def preprocess_seasonal_data(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """Parse dates and extract seasonal/temporal features."""
    df[date_col] = pd.to_datetime(df[date_col])
    df['year'] = df[date_col].dt.year
    df['month'] = df[date_col].dt.month
    df['quarter'] = df[date_col].dt.quarter
    df['day_of_week'] = df[date_col].dt.day_name()
    return df
