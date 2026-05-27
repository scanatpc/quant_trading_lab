"""Tests for risk management functions."""

import pytest
from src.backtest.risk import calculate_position_size,risk_reward_ratio,calculate_expectancy


class TestCalculatePositionSize:

    def test_basic_calculation(self):
        """账户500/风险2%/入场2100/止损2050→应买0.2个"""
        size=calculate_position_size(
            account_balance=500, risk_pct=0.02,
            entry_price=2100, stop_loss=2050
        )
        assert size==pytest.approx(0.2)

    def test_larger_stop_distance(self):
        """止损距离越大,仓位越小"""
        size=calculate_position_size(
            account_balance=1000, risk_pct=0.02,
            entry_price=2100, stop_loss=2000
        )
        assert size==pytest.approx(0.2)

    def test_zero_stop_distance(self):
        """入场价等于止损价,应返回0"""
        size=calculate_position_size(
            account_balance=500, risk_pct=0.02,
            entry_price=2100, stop_loss=2100
        )
        assert size==0


class TestRiskRewardRatio:

    def test_basic_ratio(self):
        """风险50,回报150→比率3.0"""
        ratio=risk_reward_ratio(
            entry_price=2100, stop_loss=2050, take_profit=2250
        )
        assert ratio==pytest.approx(3.0)

    def test_ratio_less_than_one(self):
        """回报小于风险的情况"""
        ratio=risk_reward_ratio(
            entry_price=2100, stop_loss=2050, take_profit=2120
        )
        assert ratio==pytest.approx(0.4)

    def test_zero_risk(self):
        """止损等于入场价,应返回0"""
        ratio=risk_reward_ratio(
            entry_price=2100, stop_loss=2100, take_profit=2200
        )
        assert ratio==0.0


class TestCalculateExpectancy:

    def test_profitable_strategy(self):
        """胜率高/盈亏比好的策略,期望值应为正"""
        trades=[
            {"pnl": 100}, {"pnl": -40}, {"pnl": 80},
            {"pnl": -30}, {"pnl": 120}, {"pnl": -50},
        ]
        result = calculate_expectancy(trades)
        assert result["total_trades"]==6
        assert result["win_rate"]>0
        assert result["expectancy"]>0

    def test_losing_strategy(self):
        """全亏的策略,期望值应为负"""
        trades=[{"pnl": -50}, {"pnl": -30}, {"pnl": -40}]
        result=calculate_expectancy(trades)
        assert result["win_rate"]==0
        assert result["expectancy"]<0

    def test_empty_trades(self):
        """空交易列表不应报错"""
        result=calculate_expectancy([])
        assert result["total_trades"]==0