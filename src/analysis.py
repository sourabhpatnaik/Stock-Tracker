"""
analysis.py

This module contains analytical utility functions used across the
Stock Tracker project.

Responsibilities:
- Perform stock-related calculations
- Keep analytical logic separate from data fetching and presentation
"""

##########################################################################
#                     STOCK PERCENTAGE CHANGE                            #
##########################################################################


def add_percentage_change(stock_data):
    
    """
    Adds a percentage change column to the stock DataFrame.

    Percentage Change Formula:
        ((Close - Open) / Open) * 100

    Parameters:
        stock_data (DataFrame): Pandas DataFrame containing stock data
                                with 'Open' and 'Close' columns

    Returns:
        DataFrame: Copy of input DataFrame with an added 'Change %' column
    """
    
    # Create a copy to avoid modifying the original DataFrame
    stock = stock_data.copy()

    # Calculate percentage change for each row
    stock["Change %"] = ((stock["Close"] - stock["Open"]) / stock["Open"] ) * 100

    # Round percentage change values to 2 decimal places
    stock["Change %"] = stock["Change %"].round(2)
    return stock



##########################################################################
#                     STOCK AVERAGE CALCULATION                          #
##########################################################################


def calculate_stock_average(stock):

    """
    Calculates average stock prices over the given dataset.

    Parameters:
        stock (DataFrame): Pandas DataFrame containing stock price columns

    Returns:
        dict: Dictionary containing average values for:
              - Open
              - High
              - Low
              - Close
    """

    return {
        "avg_open" : round(stock["Open"].mean(),2),
        "avg_high" : round(stock["High"].mean(),2),
        "avg_low" : round(stock["Low"].mean(),2),
        "avg_close" : round(stock["Close"].mean(),2)
    }