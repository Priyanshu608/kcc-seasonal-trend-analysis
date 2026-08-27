# KCC Seasonal Trend Analysis

An exploratory data analysis project studying how agricultural advisory queries change over time across **Kharif, Rabi, and Zaid** seasons using historical Kisan Call Center (KCC) data.

The project focuses on query volume, seasonal patterns, trends, and frequently requested agricultural topics.

---

## What the Project Does

* Analyzes query volume over time and across agricultural seasons
* Identifies seasonal peaks and recurring patterns
* Uses rolling averages to study underlying trends
* Analyzes queries by crop, sector, and advisory category
* Applies time-series decomposition to examine trend and seasonality
* Generates visualizations for exploratory analysis

---

## Project Structure

```text
kcc-seasonal-trend-analysis/
├── data/                  # Raw and processed data
├── docs/                  # Project documentation
├── figures/               # Generated plots
├── models/                # Saved models
├── notebooks/             # Exploratory analysis
├── src/
│   ├── data_loader.py     # Data loading and preprocessing
│   ├── trend_analysis.py  # Trend and aggregation analysis
│   └── visualize.py       # Visualization utilities
├── tests/                 # Automated tests
├── main.py                # Main analysis pipeline
├── requirements.txt       # Project dependencies
└── README.md
```

---

## Analysis Flow

```text
KCC Dataset
     ↓
Data Cleaning & Date Processing
     ↓
Time-based Aggregation
     ↓
Seasonal & Trend Analysis
     ↓
Visualization
```

---

## Key Questions

The analysis explores questions such as:

* Which months have the highest query volume?
* How does query activity differ between Kharif, Rabi, and Zaid?
* Which crops and advisory categories receive the most queries?
* Are changes in query volume driven by long-term trends or seasonal variation?

---

## Running the Project

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Place the required dataset inside the `data/` directory, then run:

```bash
python main.py
```

> **Note:** The raw dataset is not included in the repository. Make sure the required data files are available under `data/` before running the pipeline.

---

## Notes

The analysis represents **recorded KCC queries**, rather than total agricultural information demand. Missing data, inconsistent categories, and differences in reporting can affect the observed patterns.

---

## Status

The project currently focuses on **exploratory data analysis and time-series pattern discovery**. Forecasting and additional regional analysis can be explored as future extensions.
