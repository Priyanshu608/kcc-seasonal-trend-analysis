# Kisan Call Center (KCC) Seasonal Trend Analysis

An exploratory data analysis project studying how agricultural advisory queries change over time across Kharif, Rabi, and Zaid seasons.
The project focuses on query volume, seasonal patterns, trends, and frequently requested agricultural topics using historical Kisan Call Center data.

---

## What the Project Does
- Analyzes query volume across time and agricultural seasons
- Identifies seasonal peaks and recurring patterns
- Uses rolling averages to smooth short-term fluctuations
- Breaks down queries by crop, sector, and advisory category
- Applies time-series decomposition to separate trend and seasonality
- Generates visualizations to support the analysis

---

## Project Structure
\\\	ext
kcc-seasonal-trend-analysis/
+-- data/              # Raw and processed data
+-- docs/              # Project documentation
+-- figures/           # Generated plots
+-- models/            # Saved models
+-- notebooks/         # Exploratory analysis
+-- src/
¦   +-- data_loader.py     # Data loading and preprocessing
¦   +-- trend_analysis.py  # Trend and aggregation analysis
¦   +-- visualize.py       # Visualization utilities
+-- tests/             # Automated test suite
+-- main.py            # Main pipeline
+-- requirements.txt   # Dependencies
+-- README.md
\\\

---

## Analysis Flow
\\\	ext
KCC Dataset
    ?
Data Cleaning & Date Processing
    ?
Time-based Aggregation
    ?
Seasonal & Trend Analysis
    ?
Visualization
\\\

---

## Key Questions
The analysis is designed around questions such as:
- Which months have the highest query volume?
- How does demand differ between Kharif, Rabi, and Zaid?
- Which crops and advisory categories receive the most queries?
- Are observed increases part of a broader trend or seasonal variation?

---

## Running the Project

\\\ash
pip install -r requirements.txt
python main.py
\\\

> **Note:** Place the required dataset inside \data/\ before running the pipeline.

---

## Notes
The results represent recorded KCC queries, not total agricultural information demand. Missing data, inconsistent categories, and changes in reporting can affect the observed patterns.

---

## Status
Currently focused on exploratory analysis and time-series pattern discovery, with forecasting and additional regional analysis as possible future extensions.
