import yfinance as yfc
import pandas as pd
import datetime as dt
from tabulate import tabulate


##########################################################################
#                     TODAY's STOCK DETAILS                           #       
##########################################################################

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
    
    today_date = dt.datetime.now().strftime("%Y-%m-%d")
    file_name = f"{stock}_{period}_{today_date}.csv"

    # taking stock name 
    stock_name = yfc.Ticker(stock)
    
    # Getting the stock data    
    stock_data = stock_name.history(period=period)
    
    # Removing unnecessay columns for dataframe
    stock_data.drop(["Dividends","Stock Splits"],axis="columns",inplace=True)
    
    stock_data = stock_data.reset_index()
    stock_data["Date"] = stock_data["Date"].dt.date 


    # Calculating the change Percentage and then adding to new dataset
    stock_data["per_change"] = ((stock_data["Close"] - stock_data["Open"])/stock_data["Open"])*100
    stock_data["per_change"] = stock_data["per_change"].round(2)

    # Adding the "₹" symbol to ["Open","High","Low","Close"] colums for better understanding 
    price_colum = ["Open","High","Low","Close"]
    for col in price_colum:
        stock_data[col] = stock_data[col].apply(lambda x: f"₹{round(x, 2)}")

    print("Historical Stock Data:")
    print(f"Stock Name: {stock}")
    print("Period:",period)
   
   # Using Tabualte to make the table of our data for good presentation
    print(tabulate(stock_data, headers = ["Date","Open","High","Low","Close","Volume","Change %"], tablefmt = 'psql', showindex=False))

    # Asking the user if he/she want to save the file or not 
    user_save = input("Do u want to save this Data [Y/N]: ").upper()
    if user_save == "Y":
        stock_data.to_csv(f"./saved/{file_name}")
        print("Your Data has been saved in 'saved' Folder")
        
