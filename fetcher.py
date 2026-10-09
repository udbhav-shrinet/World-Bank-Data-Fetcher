#!/usr/bin/env python3
"""
World Bank Macroeconomic Ingestion & Indicator Normalization Engine
Author: Udbhav Shrinet

I developed this engine to extract, aggregate, and normalize cross-country macroeconomic
time-series indicators for empirical econometric modeling and my economics dissertation.
"""

import sys
import json
import urllib.request
import argparse
from datetime import datetime

INDICATORS = {
    'gdp_current': 'NY.GDP.MKTP.CD',
    'gdp_per_capita': 'NY.GDP.PCAP.CD',
    'gdp_growth': 'NY.GDP.MKTP.KD.ZG',
    'inflation_cpi': 'FP.CPI.TOTL.ZG',
    'unemployment': 'SL.UEM.TOTL.ZS',
    'debt_pct_gdp': 'GC.DOD.TOTL.GD.ZS',
    'co2_per_capita': 'EN.ATM.CO2E.PC',
    'trade_pct_gdp': 'NE.TRD.GNFS.ZS'
}

def fetch_indicator(country_code, indicator_code, start_year=2010, end_year=2023):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json&date={start_year}:{end_year}&per_page=100"
    req = urllib.request.Request(url, headers={'User-Agent': 'WorldBankResearchFetcher/2.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if len(data) > 1 and isinstance(data[1], list):
                records = []
                for entry in data[1]:
                    if entry.get('value') is not None:
                        records.append({
                            'year': int(entry['date']),
                            'value': float(entry['value']),
                            'country': entry['country']['value']
                        })
                return sorted(records, key=lambda x: x['year'])
    except Exception as e:
        print(f"[!] Error fetching {indicator_code} for {country_code}: {e}", file=sys.stderr)
    return []

def main():
    parser = argparse.ArgumentParser(description="World Bank Research Data Extraction Tool")
    parser.add_argument('--countries', nargs='+', default=['USA', 'IND', 'DEU', 'GBR', 'JPN'], help='ISO-3 Country Codes')
    parser.add_argument('--indicator', default='gdp_growth', choices=list(INDICATORS.keys()), help='Indicator Key')
    args = parser.parse_args()

    ind_code = INDICATORS[args.indicator]
    print(f"=== World Bank Research Ingestion: {args.indicator} ({ind_code}) ===")
    
    for c in args.countries:
        data = fetch_indicator(c, ind_code)
        if data:
            latest = data[-1]
            print(f"[{c}] {latest['country']} ({latest['year']}): {latest['value']:,.2f}")
        else:
            print(f"[{c}] No observations returned.")

if __name__ == '__main__':
    main()
