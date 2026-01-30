import yfinance as yfc
import pandas as pd
import datetime as dt
from tabulate import tabulate

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
    print("Date:",today_date)
    
    print(f"Open: ₹{latest_row["Open"]:.2f}")
    print(f"High: ₹{latest_row["High"]:.2f}")
    print(f"Low: ₹{latest_row["Low"]:.2f}")
    print(f"Close: ₹{latest_row["Close"]:.2f}")
    print(f"Volume: {latest_row["Volume"]:.2f}")
    
    if per_change > 0:
        print(f"Change: +{per_change:.2f}% \n")

    elif per_change < 0:
        print(f"Change: -{per_change:.2f}%\n")
    else:
        print(f"Change: {per_change:.2f}%\n")



##########################################################################
#                     HISTORICAL STOCK DETAILS                           #       
##########################################################################


def Get_Historical_Stock_Details(stock,period):
    stock_name = yfc.Ticker(stock)
    stock_data = stock_name.history(period=period)
    stock_data.drop(["Dividends","Stock Splits"],axis="columns",inplace=True)
    save_data = stock_data.to_csv("./data/histdata.csv")
    new_data = pd.read_csv("./data/histdata.csv")
    new_data["Date"] = pd.to_datetime(new_data["Date"])
    new_data["Date"] = new_data["Date"].dt.date 



    new_data["per_change"] = ((new_data["Close"] - new_data["Open"])/new_data["Open"])*100
    new_data["per_change"] = new_data["per_change"].round(2)

    price_colum = ["Open","High","Low","Close"]
    for col in price_colum:
        new_data[col] = new_data[col].apply(lambda x: f"₹{round(x, 2)}")

    print("Historical Stock Data:")
    print(f"Stock Name: {stock}")
    print("Period:",period)
    print(tabulate(new_data, headers = ["Date","Open","High","Low","Close","Volume","Change %"], tablefmt = 'psql', showindex=False))

    user_save = input("Do u want to save this Data [Y/N]: ").upper()
    if user_save == "Y":
        new_data.to_csv("./saved/HistoricalData.csv")
        print("Your Data has been saved in 'data' Folder")
        
    

