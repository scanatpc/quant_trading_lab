"""
Data fetching module for downloading cryptocurrency price data.

Supports multiple data sources including yfinance and ccxt.
"""

import pandas as pd
import yfinance as yf
from datetime import datetime
from typing import Optional


def fetch_crypto_data(
    symbol: str = "ETH-USD",
    start_date: str = "2024-01-01",
    end_date: Optional[str] = None,
    interval: str = "1d"
) -> pd.DataFrame:
    """
    Download cryptocurrency OHLCV data from Yahoo Finance.
    
    Args:
        symbol: Ticker symbol (e.g., 'ETH-USD', 'BTC-USD').
        start_date: Start date in 'YYYY-MM-DD' format.
        end_date: End date. Defaults to today if not specified.
        interval: Data interval ('1d', '1h', '1wk').
    
    Returns:
        DataFrame with columns: Open, High, Low, Close, Volume.
    
    Raises:
        ValueError: If no data is returned for the given parameters.
    
    Example:
        >>> eth_data = fetch_crypto_data("ETH-USD", "2024-01-01")
        >>> print(eth_data.head())
    """
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
    
    data = yf.download(symbol, start=start_date, end=end_date, interval=interval)
    
    if data.empty:
        raise ValueError(
            f"No data returned for {symbol} "
            f"from {start_date} to {end_date}"
        )
    
    # Standardize column names to lowercase
    data = yf.download(symbol, start=start_date, auto_adjust=True, multi_level_index=False)
    data.columns = [col.lower() for col in data.columns]
    
    return data


def save_data(data: pd.DataFrame, filepath: str) -> None:
    """Save DataFrame to CSV file."""
    data.to_csv(filepath)
    print(f"Data saved to {filepath} ({len(data)} rows)")


def load_data(filepath: str) -> pd.DataFrame:
    """Load DataFrame from CSV file."""
    data = pd.read_csv(filepath, index_col=0, parse_dates=True)
    print(f"Data loaded from {filepath} ({len(data)} rows)")
    return data