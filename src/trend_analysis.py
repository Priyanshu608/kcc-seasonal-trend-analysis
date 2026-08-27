import pandas as pd
import numpy as np

def calculate_monthly_call_volume(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """Aggregate total incoming query volume by year and month."""
    monthly_summary = (
        df.groupby([df[date_col].dt.year.rename('year'), df[date_col].dt.month.rename('month')])
        .size()
        .reset_index(name='call_count')
    )
    return monthly_summary

def compute_rolling_trend(series: pd.Series, window: int = 7) -> pd.Series:
    """Calculate rolling moving average to smooth short-term fluctuations."""
    return series.rolling(window=window, min_periods=1, center=True).mean()

def top_sector_queries_by_season(df: pd.DataFrame, sector_col: str, season_col: str, top_n: int = 5) -> pd.DataFrame:
    """Identify highest frequency query categories per agricultural season."""
    return (
        df.groupby([season_col, sector_col])
        .size()
        .groupby(level=0, group_keys=False)
        .nlargest(top_n)
        .reset_index(name='frequency')
    )
