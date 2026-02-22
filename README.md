# Apple Historical Price Fetcher

This project fetches historical closing prices for Apple Inc. (AAPL)
from 2025-02-10 to 2026-02-10 using YFinance.

## Setup

Create virtual environment:

    python -m venv venv
    venv\Scripts\activate  (Windows)
    source venv/bin/activate (Mac/Linux)

Install dependencies:

    pip install -r requirements.txt

## Run

Fetch data:

    python fetch_prices.py

Generate chart:

    python chart.py

Output:
- historicalPrices.json
- chart.png