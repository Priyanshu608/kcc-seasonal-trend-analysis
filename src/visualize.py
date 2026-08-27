import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

def plot_monthly_trend(df: pd.DataFrame, output_dir: str = 'figures') -> None:
    """Plot total call volume trends over time and save the figure."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='month', y='call_count', hue='year', marker='o')
    plt.title('Monthly Kisan Call Center Query Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Call Volume')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/monthly_trend.png', dpi=300)
    plt.close()

def plot_top_sectors(df: pd.DataFrame, output_dir: str = 'figures') -> None:
    """Plot top query sectors per season."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df, x='frequency', y='sector', hue='season')
    plt.title('Top Query Categories by Agricultural Season')
    plt.xlabel('Number of Inquiries')
    plt.ylabel('Sector')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/seasonal_sectors.png', dpi=300)
    plt.close()
