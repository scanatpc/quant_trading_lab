def calculate_position_size(
    account_balance:float,
    risk_pct:float,
    entry_price:float,
    stop_loss:float
)->float:
    max_loss=account_balance*risk_pct
    price_risk=abs(entry_price-stop_loss)

    if price_risk==0:
        return 0
    position_size=max_loss/price_risk
    return position_size

def risk_reward_ratio(
    entry_price:float,
    stop_loss:float,
    take_profit:float
)->float:
    risk=abs(entry_price-stop_loss)
    reward=abs(take_profit-entry_price)
    
    if risk==0:
        return 0.0
    return reward/risk

def calculate_expectancy(trades:list[dict])->dict:
    
    if not trades:
        return {
        "total_trades":0,
        "win_rate":0,
        "avg_win":0,
        "avg_loss":0,
        "profit_factor":0,
        "expectancy":0,
        "expectancy_per_dollar":0
    }
    
    wins=[t['pnl'] for t in trades if t['pnl']>0]
    losses=[t['pnl'] for t in trades if t['pnl']<=0]
    win_rate=len(wins)/len(trades)
    avg_win=sum(wins)/len(wins) if wins else 0
    avg_loss=abs(sum(losses)/len(losses)) if losses else 0
    
    expectancy=(win_rate*avg_win)-((1-win_rate)*avg_loss)
    
    return {
        "total_trades":len(trades),
        "win_rate":win_rate,
        "avg_win":avg_win,
        "avg_loss":avg_loss,
        "profit_factor":avg_win/avg_loss if avg_loss>0 else float('inf'),
        "expectancy":expectancy,
        "expectancy_per_dollar":expectancy/avg_loss if avg_loss>0 else 0
    }
