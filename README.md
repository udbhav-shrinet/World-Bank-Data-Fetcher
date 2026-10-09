# World Bank Macroeconomic Data Fetcher & Econometric Normalization Suite

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Interactive Studio](https://img.shields.io/badge/live%20studio-GitHub%20Pages-amber.svg)](https://udbhav-shrinet.github.io/World-Bank-Data-Fetcher/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> I developed this data extraction and harmonization engine to extract, aggregate, and normalize cross-country macroeconomic time-series indicators for empirical econometric analysis in my economics dissertation.

---

## 🏛️ Live Research Studio

👉 **[Launch Macroeconomic Interactive Explorer](https://udbhav-shrinet.github.io/World-Bank-Data-Fetcher/)**

---

## 📊 Core Capabilities

- **Real-Time World Bank API Ingestion**: Direct connectivity with the World Bank Open Data v2 REST API without requiring auth tokens or manual batch downloads.
- **Multidimensional Indicator Harmonization**:
  - Growth Dynamics: GDP Growth (annual %), Gross Fixed Capital Formation
  - Economic Output: Nominal GDP, Real GDP, GDP per capita (PPP & current USD)
  - Price & Monetary Pressures: CPI Inflation, Broad Money growth
  - Labor & Productivity: Total Unemployment, Youth Unemployment, Labor Participation
  - Ecological Sustainability: CO2 emissions per capita, Renewable energy consumption
- **Empirical Ranking Matrix**: Generates a unified composite macroeconomic resilience score across selected nation cohorts.
- **Python Research Tool (`fetcher.py`)**: Scriptable CLI to pull historical time-series directly into tabular pandas structures for regression and econometric analysis.

---

## 🛠️ CLI Usage

```bash
# Clone the repository
git clone https://github.com/udbhav-shrinet/World-Bank-Data-Fetcher.git
cd World-Bank-Data-Fetcher

# Query GDP growth for country cohort
python fetcher.py --countries USA IND DEU JPN GBR --indicator gdp_growth
```

---

## 📄 License

MIT License. Designed for academic research, empirical economics, and macroeconomic analysis.
