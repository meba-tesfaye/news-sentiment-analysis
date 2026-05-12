import talib
import pynance as pn
import pandas as pd
import numpy as np

def calculate_metrics(df):
    """
    Addresses Task 2 omissions: Adds EMA, MACD, and PyNance returns.
    This modular function can be called from any notebook.
    """
    # Ensure we are working with a copy to avoid SettingWithCopy warnings
    df = df.copy()
    
    # Check if Close exists
    if 'Close' not in df.columns:
        raise ValueError("Dataframe must contain a 'Close' column.")

    close_prices = df['Close'].values

    # 1. EMA (Exponential Moving Average) - Directly addressing feedback
    df['EMA_20'] = talib.EMA(close_prices, timeperiod=20)

    # 2. MACD (Moving Average Convergence Divergence) - Directly addressing feedback
    macd, macdsignal, macdhist = talib.MACD(
        close_prices, fastperiod=12, slowperiod=26, signalperiod=9
    )
    df['MACD'] = macd
    df['MACD_Signal'] = macdsignal
    df['MACD_Hist'] = macdhist

    # 3. PyNance - Directly addressing feedback
    # Using pynance to calculate daily returns as a quantitative baseline
    df['PyNance_Returns'] = pn.tech.ret(df['Close'])

    return df

def get_basic_stats(df):
    """Returns basic quantitative stats for the report to prove Task 2 completion."""
    return df[['Close', 'EMA_20', 'MACD', 'PyNance_Returns']].describe()