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

    print("STOCK DETAILS:")    
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
#                     SHORT TERM STOCK DETAILS                           #       
##########################################################################


def Get_Short_Term_Stock_Details(stock,period):
    
    """
    Fetches short-term historical stock data, calculates price changes and averages,
    displays the data in a formatted table, and optionally saves it to a CSV file.

    This function uses Yahoo Finance to retrieve historical stock price data for a 
    given stock ticker and time period. It cleans the dataset, calculates percentage 
    change in price, computes average prices, formats the output for readability, 
    and presents the data in a tabular format. The user is also given an option to 
    save the processed data as a CSV file.

    Parameters
    ----------
    stock : str
        The stock ticker symbol (e.g., "TCS.NS", "INFY.NS", "AAPL").
    
    period : str
        The time period for fetching historical data (e.g., "5d", "1mo", "3mo", "1y").

    Returns
    -------
    None
        This function does not return any value. It prints the processed stock data,
        summary statistics, and optionally saves the data to a CSV file.

    Features
    --------
    - Fetches historical stock data using Yahoo Finance.
    - Removes unnecessary columns like dividends and stock splits.
    - Calculates daily percentage price change.
    - Computes average open, high, low, and close prices.
    - Formats price values with the ₹ symbol.
    - Displays data in a well-formatted table using `tabulate`.
    - Allows the user to save the processed data as a CSV file.

    Example
    -------
     Get_Short_Term_Stock_Details("TCS.NS", "1mo")
    """
        
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

    avg_open = round(stock_data["Open"].mean(), 2)
    avg_high = round(stock_data["High"].mean(), 2)
    avg_low = round(stock_data["Low"].mean(), 2)
    avg_close = round(stock_data["Close"].mean(), 2)



    # Adding the "₹" symbol to ["Open","High","Low","Close"] colums for better understanding 
    price_colum = ["Open","High","Low","Close"]
    for col in price_colum:
        stock_data[col] = stock_data[col].apply(lambda x: f"₹{round(x, 2)}")

    print("Historical Stock Data:")
    print(f"Stock Name: {stock}")
    print("Period:",period)
   
   # Using Tabualte to make the table of our data for good presentation
    print(tabulate(stock_data, headers = ["Date","Open","High","Low","Close","Volume","Change %"], tablefmt = 'psql', showindex=False))

    print()
    print("Stock Summary:")
    print(f"Average Open Price: ₹{avg_open}")
    print(f"Average High Price: ₹{avg_high}")
    print(f"Average Low Price: ₹{avg_low}")
    print(f"Average Close Price: ₹{avg_close}")
    print()

    # Asking the user if he/she want to save the file or not 
    user_save = input("Do u want to save this Data [Y/N]: ").upper()
    if user_save == "Y":
        stock_data.to_csv(f"./saved/{file_name}",encoding="utf-8-sig")
        print("Your Data has been saved in 'saved' Folder")


##########################################################################
#                     MULTIPLE STOCK DETAILS                           #       
##########################################################################

def Get_Multiple_Stock_Details(stock_list):
    
    """
    Fetches and displays the latest stock data for multiple stocks, calculates 
    percentage price changes, and presents the results in a formatted table.

    This function retrieves the most recent (1-day) historical stock data for a 
    list of stock tickers using Yahoo Finance. It restructures the downloaded 
    data into a row-wise format, calculates the percentage change between open 
    and close prices, formats price values with the rupee symbol (₹), and displays 
    the final dataset in a tabular format using `tabulate`.

    Parameters
    ----------
    stock_list : list[str]
        A list of stock ticker symbols (e.g., ["TCS.NS", "INFY.NS", "ITC.NS"]).

    Returns
    -------
    None
        This function does not return any value. It prints the processed stock 
        details directly to the console.

    Features
    --------
    - Downloads latest stock data for multiple tickers using Yahoo Finance.
    - Converts multi-index column data into a structured row-wise DataFrame.
    - Calculates daily percentage price change for each stock.
    - Formats price columns with the ₹ symbol for better readability.
    - Displays the final data in a well-formatted table using `tabulate`.

    Example
    -------
    >>> Get_Multiple_Stock_Details(["TCS.NS", "INFY.NS", "ITC.NS"])
    """

    # GETTING DATA FROM YFINANCE
    gStock = yfc.download(stock_list,period="1d")
    
    # RESETING INDEX AND CONVERTING DATE COLUMN INTO DATE FORMAT
    gStock = gStock.reset_index()
    gStock["Date"] = gStock["Date"].dt.date

    
    rows = []

    # CONVERTING COLUMN DATA INTO ROWS 
    for stock in stock_list:
        temp = pd.DataFrame({
            "Date": gStock["Date"],
            "Stock": stock,
            "Open": gStock[("Open",stock)],
            "High": gStock[("High",stock)],
            "Low": gStock[("Low",stock)],
            "Close" : gStock[("Close",stock)],
            "Volume": gStock[("Volume",stock)]
        })

        temp["Change %"] = ((temp["Close"] - temp["Open"]) / temp["Open"]) * 100
        rows.append(temp)
    final_stock = pd.concat(rows) 

    # ADDING THE RUPEES SIGN
    price_col = ["Open","High","Low","Close"]
    for col in price_col:
        final_stock[col] = final_stock[col].apply(lambda x: f"₹{round(x,2)}")

    # DISPLAYING THE FINAL DATA
    print()
    print("Multiple Stocks Details:")
    print(tabulate(final_stock, headers=["Date","Stock Name","Open","High","Low","Close","Volume","Change %"], tablefmt="psql",showindex=False))
    print()



##########################################################################
#                     MULTIPLE STOCK DETAILS                           #       
##########################################################################


def Get_Historical_Stock_Details(stock,start_date,end_date):

    today_date = dt.datetime.now().strftime("%Y-%m-%d")
    file_name = f"{stock}_{today_date}.csv"

    stock_data = yfc.download(stock,start=start_date,end=end_date)
    stock_data.columns = stock_data.columns.droplevel(1)
    stock_data.columns.name = None
    stock_data = stock_data.reset_index()
    stock_data["Date"] = stock_data["Date"].dt.date

    sym_col = ["Close","High","Low","Open"]
    for col in sym_col:
        stock_data[col] = stock_data[col].apply(lambda x: f"₹{round(x,2)}")
    
    print("Historical Stock Details:")
    print()
    print("Stock Name:",stock)
    print()
    print(tabulate(stock_data,headers=["Date","Close","High","Low","Open","Volume"], tablefmt="psql", showindex=False))

    save_inp = (input("Do You Want to Save this Data (Y/N): ")).upper()
    if save_inp == "Y":
        stock_data.to_csv(f"./saved/{file_name}",encoding="utf-8-sig")
        print("Your Data has been saved in 'saved' Folder")



