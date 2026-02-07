"""
formatter.py

This module contains formatting utility functions used to prepare
stock data for display purposes.

Responsibilities:
- Format currency values with the Indian Rupee symbol
- Format percentage change values for user-friendly output

Note:
These functions should be used only for presentation,
not before performing numerical analysis.
"""


##########################################################################
#                     CURRENCY FORMATTING                                #
##########################################################################


def format_currency(stock_data):

    """
    Formats stock price columns by adding the Indian Rupee symbol.

    Columns formatted:
        - Open
        - High
        - Low
        - Close

    Parameters:
        stock_data (DataFrame): Pandas DataFrame containing stock price data

    Returns:
        DataFrame: Copy of DataFrame with formatted currency values
    """

    # Create a copy to avoid mutating the original DataFrame
    stock = stock_data.copy()

    # Add Rupee symbol and round values to 2 decimal places
    for col in ["Open","High","Low","Close"]:
        stock[col] = stock[col].apply(lambda x: f"₹{round(x,2)}")

    return stock



##########################################################################
#                     PERCENTAGE FORMATTING                              #
##########################################################################


def format_change(stock_data):

    """
    Formats percentage change column by appending '%' symbol.

    Columns formatted:
        - Change %

    Parameters:
        stock_data (DataFrame): Pandas DataFrame containing percentage data

    Returns:
        DataFrame: Copy of DataFrame with formatted percentage values
    """

    # Create a copy to avoid mutating the original DataFrame
    stock = stock_data.copy()

    # Append percentage symbol to percentage values
    for col in ["Change %"]:
        stock[col] = stock[col].apply(lambda x: f"{round(x,2)} %")
        
    return stock