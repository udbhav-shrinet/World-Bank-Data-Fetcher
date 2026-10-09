# World Bank Open Data Extraction & Macroeconomic Analytics Engine

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Interactive Demo](https://img.shields.io/badge/demo-GitHub%20Pages-blue.svg)](https://udbhav-shrinet.github.io/World-Bank-Data-Fetcher/)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> Automated programmatic ingestion pipeline and interactive dashboard for World Bank macroeconomic time-series indicators (GDP, Inflation, Population, CO2 Emissions).

---

## 🚀 Live Interactive Showcase

Query real-time macroeconomic indicators across global economies:  
👉 **[Launch World Bank Data Studio](https://udbhav-shrinet.github.io/World-Bank-Data-Fetcher/)**

---

## ✨ Key Features

- **Multi-Indicator REST Client**: High-throughput querying for World Bank API v2 with support for 16,000+ development metrics.
- **Automated Data Normalization**: Cleans, sorts, and structures nested JSON responses into Pandas DataFrames and CSV formats.
- **Dual Runtime Architecture**:
  - **Python CLI Tool (`fetcher.py`)**: For automated backend ETL and cron pipelines.
  - **Google Apps Script (`wbdf.gs`)**: For direct spreadsheet automation inside Google Sheets.
- **Interactive Visual Studio**: Client-side dashboard for cross-country comparative time-series visualization.

---

## 🛠️ System Architecture

```text
┌─────────────────────────┐       ┌────────────────────────┐       ┌──────────────────────┐
│  Country Code / Indicator│ ───>  │  World Bank API Gateway │ ───>  │  Data Sanitization   │
│  e.g., USA, IND / GDP   │       │  v2 JSON REST Endpoint │       │   (Pandas Engine)    │
└─────────────────────────┘       └────────────────────────┘       └──────────┬───────────┘
                                                                              │
                                                   ┌──────────────────────────┴──────────────────────────┐
                                                   ▼                                                     ▼
                                       ┌─────────────────────────┐                           ┌───────────────────────┐
                                       │   Structured CSV Export │                           │  GitHub Pages Studio  │
                                       │  Time-Series Datasets   │                           │  Interactive Web App  │
                                       └─────────────────────────┘                           └───────────────────────┘
```

---

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/udbhav-shrinet/World-Bank-Data-Fetcher.git
   cd World-Bank-Data-Fetcher
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage & CLI Reference

### Fetch Country GDP
```bash
python fetcher.py --country US --indicator gdp --start 2010 --end 2024 --export
```

### Compare Inflation or Population
```bash
python fetcher.py --country IN --indicator inflation --export
```

### Supported Indicator Keys
- `gdp`: GDP in current US Dollars
- `gdp_growth`: Annual GDP Growth Percentage
- `inflation`: Consumer Price Index Inflation %
- `population`: Total National Population
- `co2`: CO2 Emissions (Metric tons per capita)
- `unemployment`: Total Unemployment %

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
