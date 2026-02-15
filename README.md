# KL & Selangor House Rental Predictive Analysis

A Streamlit web application that analyzes apartment rental data in Kuala Lumpur and Selangor, and predicts monthly rent prices using a Random Forest machine learning model.

## Features

### Dashboard
- **Metric Cards** — Total listings, average rent, median rent, and total locations
- **Interactive Filters** — Filter by region (KL/Selangor) and property type
- **Line Chart** — Average monthly rent trend by completion year per region
- **Bar Chart** — Average monthly rent comparison by property type per region
- **Data Table** — Browse all rental listings with key property details

### Predictor
- **Rental Price Prediction** — Input property details and get an estimated monthly rent
- **10 Input Features** — Region, location, property type, furnished status, size, rooms, bathroom, parking, facilities count
- **Live Filtering** — Location dropdown updates dynamically based on selected region

## Dataset

- **Source**: Mudah.my apartment listings
- **Size**: 19,043 listings
- **Coverage**: Kuala Lumpur and Selangor
- **Features**: 16 columns including property name, rent, location, type, size, rooms, furnished status, and facilities

## Model Performance

| Metric | Value |
|--------|-------|
| **Algorithm** | Random Forest Regressor |
| **MAE** | RM 208.93 |
| **RMSE** | RM 340.82 |
| **R² Score** | 0.754 |

### Top Feature Importance
1. Size (sq.ft) — 31.8%
2. Furnished status — 25.3%
3. Location — 16.6%
4. Property type — 9.9%
5. Facilities count — 6.0%

## Project Structure

```
├── Dashboard.py              # Main dashboard page
├── pages/
│   └── 1_Predictor.py        # Rental price predictor page
├── notebook/
│   ├── model.ipynb            # Model training notebook
│   └── chart_plotting.ipynb   # Data visualization notebook
├── data/
│   ├── mudah-apartment-kl-selangor.csv           # Raw data
│   └── mudah-apartment-kl-selangor-cleaned.csv   # Cleaned data
├── model/
│   ├── random_forest_model.joblib   # Trained model
│   └── label_encoders.joblib        # Label encoders
├── .streamlit/
│   └── config.toml            # Dark theme configuration
└── requirement.txt
```

## Getting Started

### Prerequisites
- Python 3.10+

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/syahirisyraf/kl-selangor-rental-predictive-analysis.git
   cd kl-selangor-rental-predictive-analysis
   ```

2. Create a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install streamlit pandas numpy scikit-learn joblib
   ```

4. Train the model (if model files are not present)
   - Open and run all cells in `notebook/model.ipynb`

5. Run the app
   ```bash
   streamlit run Dashboard.py
   ```

## Tech Stack

- **Frontend**: Streamlit 1.54
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn 1.8 (Random Forest Regressor)
- **Model Serialization**: Joblib