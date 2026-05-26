# Quant Trading Lab

A quantitative trading strategy research and backtesting system
built with Python.

## Overview

This project implements a complete quantitative trading workflow:
- Historical data acquisition and processing
- Technical indicator library (EMA, RSI, MACD, Bollinger Bands, etc.)
- Multiple classic trading strategies
- Event-driven backtesting engine
- Statistical validation and performance analysis

## Project Structure

quant-trading-lab/
├── src/
│   ├── data/           # Data fetching and processing
│   ├── indicators/     # Technical indicator implementations
│   ├── strategies/     # Trading strategy implementations
│   ├── backtest/       # Backtesting engine
│   └── visualization/  # Charts and reports
├── tests/              # Unit tests
├── notebooks/          # Jupyter analysis notebooks
├── docs/               # Documentation
└── data/               # Local data storage (not tracked)

## Tech Stack

- **Language**: Python 3.11+
- **Data Processing**: pandas, NumPy
- **Visualization**: Plotly, Matplotlib
- **Data Sources**: yfinance, ccxt
- **Testing**: pytest

## Getting Started

1. Clone the repository
   ```bash
   git clone git@github.com:yourname/quant-trading-lab.git
   cd quant-trading-lab
   ```

2. Set up virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run tests
   ```bash
   pytest tests/ -v
   ```

## Status

🚧 Under active development

## License

MIT License
