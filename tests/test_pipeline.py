import unittest
import pandas as pd
from src.data_loader import preprocess_seasonal_data
from src.trend_analysis import calculate_monthly_call_volume

class TestKCCPipeline(unittest.TestCase):
    def setUp(self):
        self.sample_df = pd.DataFrame({
            'CreatedOn': ['2025-01-15 10:00:00', '2025-01-20 14:00:00', '2025-02-05 09:00:00'],
            'Sector': ['Agriculture', 'Agriculture', 'Horticulture'],
            'Crop': ['Wheat', 'Wheat', 'Tomato']
        })

    def test_preprocessing_features(self):
        processed = preprocess_seasonal_data(self.sample_df.copy(), date_col='CreatedOn')
        self.assertIn('year', processed.columns)
        self.assertIn('month', processed.columns)
        self.assertIn('quarter', processed.columns)
        self.assertEqual(processed['month'].iloc[0], 1)

    def test_monthly_volume_aggregation(self):
        processed = preprocess_seasonal_data(self.sample_df.copy(), date_col='CreatedOn')
        monthly_summary = calculate_monthly_call_volume(processed, date_col='CreatedOn')
        jan_count = monthly_summary[monthly_summary['month'] == 1]['call_count'].values[0]
        self.assertEqual(jan_count, 2)

if __name__ == '__main__':
    unittest.main()
