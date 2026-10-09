"""
World Bank Data Fetcher & Indicator Analytics Engine
High-throughput automated client for querying World Bank Open Data APIs, normalizing macroeconomic indicators, and generating structured time-series datasets.
"""

import argparse
import sys
import json
import requests
import pandas as pd
from datetime import datetime

INDICATOR_MAP = {
    "gdp": ("NY.GDP.MKTP.CD", "GDP (current US$)"),
    "gdp_growth": ("NY.GDP.MKTP.KD.ZG", "GDP growth (annual %)"),
    "inflation": ("FP.CPI.TOTL.ZG", "Inflation, consumer prices (annual %)"),
    "population": ("SP.POP.TOTL", "Population, total"),
    "co2": ("EN.ATM.CO2E.PC", "CO2 emissions (metric tons per capita)"),
    "unemployment": ("SL.UEM.TOTL.ZS", "Unemployment, total (% of total labor force)")
}

BASE_URL = "http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&date={date_range}&per_page=1000"

def fetch_indicator(country_code, indicator_key, start_year=2010, end_year=2024):
    if indicator_key not in INDICATOR_MAP:
        raise ValueError(f"Unknown indicator '{indicator_key}'. Choose from: {list(INDICATOR_MAP.keys())}")
    
    ind_id, ind_name = INDICATOR_MAP[indicator_key]
    date_range = f"{start_year}:{end_year}"
    url = BASE_URL.format(country=country_code.lower(), indicator=ind_id, date_range=date_range)
    
    print(f"[*] Fetching '{ind_name}' for country '{country_code.upper()}' ({date_range})...")
    resp = requests.get(url, timeout=20)
    if resp.status_code != 200:
        print(f"[!] HTTP Error {resp.status_code}: {resp.text}")
        return None
        
    data = resp.json()
    if len(data) < 2 or not data[1]:
        print(f"[!] No data records found for {country_code} ({indicator_key}).")
        return None
        
    records = []
    for item in data[1]:
        val = item.get("value")
        year = item.get("date")
        if val is not None:
            records.append({
                "Country": item.get("country", {}).get("value", country_code),
                "CountryCode": country_code.upper(),
                "Year": int(year),
                "Indicator": ind_name,
                "IndicatorCode": ind_id,
                "Value": float(val)
            })
            
    df = pd.DataFrame(records).sort_values("Year")
    print(f"[+] Retrieved {len(df)} validated observations.")
    return df

def export_records(df, filename_prefix="world_bank_data"):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_name = f"{filename_prefix}_{ts}.csv"
    df.to_csv(csv_name, index=False)
    print(f"[+] Successfully exported data to {csv_name}")

def main():
    parser = argparse.ArgumentParser(description="World Bank Open Data Automated Extraction Engine")
    parser.add_argument("-c", "--country", default="US", help="ISO-2 or ISO-3 country code (e.g. US, IN, DE, CN, GBR, WLD)")
    parser.add_argument("-i", "--indicator", default="gdp", choices=list(INDICATOR_MAP.keys()), help="Macroeconomic indicator")
    parser.add_argument("-s", "--start", type=int, default=2010, help="Start year")
    parser.add_argument("-e", "--end", type=int, default=2024, help="End year")
    parser.add_argument("-o", "--export", action="store_true", help="Export to CSV file")
    
    args = parser.parse_args()
    df = fetch_indicator(args.country, args.indicator, args.start, args.end)
    if df is not None and not df.empty:
        print("
=== Recent Data Preview ===")
        print(df.tail(10).to_string(index=False))
        if args.export:
            export_records(df, f"wb_{args.country}_{args.indicator}")

if __name__ == "__main__":
    main()
