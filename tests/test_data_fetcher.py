"""Tests for the data fetcher module."""

import pandas as pd
import pytest
from src.data.fetcher import fetch_crypto_data


class TestFetchCryptoData:
    """Test suite for fetch_crypto_data function."""
    
    def test_returns_dataframe(self):
        """Should return a pandas DataFrame."""
        data = fetch_crypto_data("ETH-USD", "2024-01-01", "2024-01-31")
        assert isinstance(data, pd.DataFrame)
    
    def test_has_required_columns(self):
        """Should contain OHLCV columns."""
        data = fetch_crypto_data("ETH-USD", "2024-01-01", "2024-01-31")
        required = ['open', 'high', 'low', 'close', 'volume']
        for col in required:
            assert col in data.columns, f"Missing column: {col}"
    
    def test_data_not_empty(self):
        """Should return non-empty data for valid parameters."""
        data = fetch_crypto_data("ETH-USD", "2024-01-01", "2024-01-31")
        assert len(data) > 0
    
    def test_high_greater_than_low(self):
        """High price should always be >= low price."""
        data = fetch_crypto_data("ETH-USD", "2024-01-01", "2024-06-01")
        assert (data['high'] >= data['low']).all()
    
    def test_invalid_symbol_raises_error(self):
        """Should raise ValueError for invalid symbol."""
        with pytest.raises(ValueError):
            fetch_crypto_data("INVALID-SYMBOL-XYZ", "2024-01-01", "2024-01-31")
    
    def test_close_within_high_low_range(self):
        """Close price should be between high and low."""
        data = fetch_crypto_data("ETH-USD", "2024-01-01", "2024-06-01")
        assert (data['close'] <= data['high']).all()
        assert (data['close'] >= data['low']).all()