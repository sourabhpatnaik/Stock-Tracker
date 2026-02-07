import yfinance as yfc
import pandas as pd
from utils import normalize_stock,normalize_multiple_stock

"""
stock_api.py

This module provides utility functions to fetch stock market data
using the yfinance library.

Supported features:
- Fetch today's stock details
- Fetch short-term stock data (e.g., 3d, 7d, 1mo)
- Fetch multiple stocks data at once
- Fetch historical stock data for a given date range

All stock symbols are normalized before fetching data.
"""

##########################################################################
#                     TODAY's STOCK DETAILS                           #       
##########################################################################

def Get_Today_Stock_Detail(stock):
    
    """
    Fetches today's stock data for a given stock symbol.

    Parameters:
        stock (str): Stock symbol (e.g., 'itc', 'reliance')

    Returns:
        tuple:
            - normalized stock symbol (str)
            - pandas DataFrame containing today's stock data
    """
    # Normalize stock symbol (adds .NS if required, uppercase, etc.)
    stock = normalize_stock(stock)
    
    # Create yfinance Ticker object
    stock_name = yfc.Ticker(stock)
   
    # Fetch today's stock data 
    stock_data = stock_name.history(period="1d")

    return stock,stock_data



##########################################################################
#                     SHORT TERM STOCK DETAILS                           #       
##########################################################################


def Get_Short_Term_Stock_Details(stock,period):

    """
    Fetches short-term stock data for a given stock symbol.

    Parameters:
        stock (str): Stock symbol (e.g., 'itc')
        period (str): Time period ('3d', '7d', '1mo', etc.)

    Returns:
        tuple:
            - normalized stock symbol (str)
            - pandas DataFrame containing short-term stock data
    """

    # Normalize stock symbol    
    stock = normalize_stock(stock)
    
    # Create yfinance Ticker object 
    stock_name = yfc.Ticker(stock)
    
    # Fetch stock data for the given period    
    stock_data = stock_name.history(period=period)
    
    # Removing unnecessay columns from dataframe
    stock_data.drop(["Dividends","Stock Splits"],axis="columns",inplace=True)
    
    # Reset index to convert Date from index to column
    stock_data = stock_data.reset_index()
    
    # Convert datetime to date only
    stock_data["Date"] = stock_data["Date"].dt.date 

    return stock,stock_data


##########################################################################
#                     MULTIPLE STOCK DETAILS                           #       
##########################################################################

def Get_Multiple_Stock_Details(stock_list):

    """
    Fetches today's stock data for multiple stock symbols.

    Parameters:
        stock_list (list): List of stock symbols

    Returns:
        pandas DataFrame containing combined stock data for all stocks
    """

    # Normalize multiple stock symbols
    stock_list = normalize_multiple_stock(stock_list)

    # Fetch stock data for all stocks at once
    gStock = yfc.download(stock_list,period="1d")
    
    # RESETING INDEX AND CONVERTING DATE COLUMN INTO DATE FORMAT
    gStock = gStock.reset_index()
    gStock["Date"] = gStock["Date"].dt.date


    rows = []

    # Convert multi-index columns into row-wise stock data 
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

        # Calculate percentage change for each stock
        temp["Change %"] = ((temp["Close"] - temp["Open"]) / temp["Open"]) * 100
        rows.append(temp)

    # Combine all stocks data into a single DataFrame
    final_stock = pd.concat(rows)

    return final_stock 



##########################################################################
#                     HISTORICAL STOCK DETAILS                           #       
##########################################################################


def Get_Historical_Stock_Details(stock,start_date,end_date):

    """
    Fetches historical stock data for a given date range.

    Parameters:
        stock (str): Stock symbol
        start_date (str): Start date (YYYY-MM-DD)
        end_date (str): End date (YYYY-MM-DD)

    Returns:
        tuple:
            - normalized stock symbol (str)
            - pandas DataFrame containing historical stock data
    """
    
    # Normalize stock symbol
    stock = normalize_stock(stock)

    # Fetch historical stock data
    stock_data = yfc.download(stock,start=start_date,end=end_date)

    # Remove multi-level column indexing
    stock_data.columns = stock_data.columns.droplevel(1)
    stock_data.columns.name = None

    # Reset index and format Date column
    stock_data = stock_data.reset_index()
    stock_data["Date"] = stock_data["Date"].dt.date

    return stock,stock_data


