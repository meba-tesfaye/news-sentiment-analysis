def get_technical_indicators(df):
    df = df.copy()
    
    # 1. Clean the 'Close' column
    # This converts everything to numbers and turns "AAPL" (text) into NaN (empty)
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    
    # 2. Drop any rows that became empty (like the header row with 'AAPL')
    df = df.dropna(subset=['Close'])
    
    # 3. Now the math will work perfectly
    # EMA
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    
    # MACD
    ema_12 = df['Close'].ewm(span=12, adjust=False).mean()
    ema_26 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = ema_12 - ema_26
    
    # Returns
    df['Daily_Returns'] = df['Close'].pct_change()
    
    return df