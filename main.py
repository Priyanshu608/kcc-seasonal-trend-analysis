import argparse
from pathlib import Path
from src.data_loader import load_dataset, preprocess_seasonal_data
from src.trend_analysis import calculate_monthly_call_volume, compute_rolling_trend
from src.visualize import plot_monthly_trend

def run_pipeline(data_path: str, output_dir: str = 'figures') -> None:
    print(f"Loading data from: {data_path}")
    df = load_dataset(data_path)
    
    print("Preprocessing date features...")
    df = preprocess_seasonal_data(df, date_col='CreatedOn')
    
    print("Computing seasonal call volumes...")
    monthly_trends = calculate_monthly_call_volume(df, date_col='CreatedOn')
    monthly_trends['rolling_avg'] = compute_rolling_trend(monthly_trends['call_count'])
    
    print(f"Saving visualization artifacts to /{output_dir}...")
    plot_monthly_trend(monthly_trends, output_dir=output_dir)
    print("Pipeline execution complete.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='KCC Seasonal Trend Analysis Pipeline')
    parser.add_argument('--data', type=str, default='data/kcc_sample.csv', help='Path to dataset CSV')
    parser.add_argument('--output', type=str, default='figures', help='Output directory for plots')
    args = parser.parse_args()
    
    run_pipeline(args.data, args.output)
