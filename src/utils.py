"""
utils.py

This module contains helper utility functions used across the
Stock Tracker project.

Responsibilities:
- Normalize stock symbols
- Ensure consistent stock naming conventions
"""

##########################################################################
#                     SINGLE STOCK NORMALIZATION                         #
##########################################################################

def normalize_stock(stock):

    """
    Normalizes a single stock symbol.

    - Removes leading/trailing whitespace
    - Converts the symbol to uppercase
    - Appends '.NS' if not already present

    Parameters:
        stock (str): Stock symbol (e.g., 'itc', 'Itc.ns')

    Returns:
        str: Normalized stock symbol (e.g., 'ITC.NS')
    """

    # Remove extra spaces and convert to uppercase
    stock = stock.strip().upper()

    # Append '.NS' if not already present
    if not stock.endswith(".NS"):
        stock = stock + ".NS"

    return stock


##########################################################################
#                     MULTIPLE STOCK NORMALIZATION                       #
##########################################################################


def normalize_multiple_stock(stock_list):

    """
    Normalizes a list of stock symbols.

    - Removes whitespace
    - Converts each symbol to uppercase
    - Appends '.NS' if missing

    Parameters:
        stock_list (list): List of stock symbols

    Returns:
        list: List of normalized stock symbols
    """

    # List to store normalized stock symbols
    new_stock_list = []

    # Normalize each stock symbol
    for stock in stock_list:
        stock = stock.strip().upper()
        if not stock.endswith(".NS"):
            stock += ".NS"
            new_stock_list.append(stock)
        else:
            new_stock_list.append(stock)
            
    return new_stock_list