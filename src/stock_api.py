import yfinance as yfc

def Get_Today_Stock_Detail(stock):

    """
    Fetches and displays today's stock market data for a given stock symbol
    using Yahoo Finance.

    This function retrieves the latest available trading data for the
    specified stock, including Open, High, Low, Close prices, trading
    volume, and percentage change between Open and Close.

    Parameters:
    ----------
    stock : str
        Stock symbol in Yahoo Finance format.
        Example: 'TATASTEEL.NS'

    Output:
    -------
    Prints the following details to the console:
    - Stock symbol
    - Trading date
    - Open price
    - High price
    - Low price
    - Close price
    - Volume
    - Percentage change from Open to Close

    Notes:
    ------
    - Data is fetched using the `yfinance` library.
    - Percentage change is calculated as:
      ((Close - Open) / Open) * 100
    - If no data is available, the caller should handle the exception.
    """

    # Getting the Stock from yfinance
    stock_name = yfc.Ticker(stock)
   
    # Storing the data 
    stock_data = stock_name.history(period="1d")
    
    # Selecting teh latest row from the data 
    latest_row = stock_data.iloc[-1]
    
    # Selecting the Date
    today_date = latest_row.name.date()
    
    # Calculating the Change
    per_change = ((latest_row["Close"] - latest_row["Open"])/latest_row["Open"])*100
        
    print("Stock:",stock)
    print("Date:",today_date,"\n")
    
    print(f"Open: ₹{latest_row["Open"]:.2f}")
    print(f"High: ₹{latest_row["High"]:.2f}")
    print(f"Low: ₹{latest_row["Low"]:.2f}")
    print(f"Close: ₹{latest_row["Close"]:.2f}")
    print(f"Volume: {latest_row["Volume"]:.2f}")
    
    if per_change > 0:
        print(f"Change: +{per_change:.2f}%")

    elif per_change < 0:
        print(f"Change: -{per_change:.2f}%")
    else:
        print(f"Change: {per_change:.2f}%")
    
