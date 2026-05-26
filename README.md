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

quant-trading-lab/<br>
├── src/<br>
│   ├── data/           # Data fetching and processing<br>
│   ├── indicators/     # Technical indicator implementations<br>
│   ├── strategies/     # Trading strategy implementations<br>
│   ├── backtest/       # Backtesting engine<br>
│   └── visualization/  # Charts and reports<br>
├── tests/              # Unit tests<br>
├── notebooks/          # Jupyter analysis notebooks<br>
├── docs/               # Documentation<br>
└── data/               # Local data storage (not tracked)<br>

## Tech Stack

- **Language**: Python 3.11+
- **Data Processing**: pandas, NumPy
- **Visualization**: Plotly, Matplotlib
- **Data Sources**: yfinance, ccxt
- **Testing**: pytest

## Getting Started

1. Clone the repository
   ```bash
   git clone git@github.com:scanatpc/quant_trading_lab.git
   cd quant_trading_lab
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

Under active development

## License

MIT License
