from stock_api import Get_Today_Stock_Detail,Get_Short_Term_Stock_Details,Get_Multiple_Stock_Details,Get_Historical_Stock_Details
from analysis import add_percentage_change,calculate_stock_average
from formatter import format_currency,format_change
from tabulate import tabulate
import datetime as dt

"""
main.py

This module acts as the main controller / presentation layer
for the Stock Tracker project.

Responsibilities:
- Calls stock_api functions to fetch stock data
- Applies analysis and formatting
- Displays results in a user-friendly tabular format
- Handles user interaction (printing and saving CSV files)

No data-fetching or business logic is implemented here directly.
"""

##########################################################################
#                     TODAY'S STOCK DETAILS                              #
##########################################################################

def print_today_stock(stock_name):

    """
    Displays today's stock details for a given stock symbol.

    Parameters:
        stock_name (str): Stock symbol (e.g., 'itc')

    Returns:
        None
    """

    # Fetch today's stock data
    stock_N,stock_data = Get_Today_Stock_Detail(stock_name)

     # Remove unnecessary columns
    stock_data = stock_data.drop(columns=["Dividends","Stock Splits"])

    # Reset index and format Date column
    stock_data = stock_data.reset_index()
    stock_data["Date"] = stock_data["Date"].dt.date

    # Calculate percentage change
    stock_data = add_percentage_change(stock_data)

    # Get the latest stock record
    latest = stock_data.iloc[-1]
    
     # Display stock details
    print()
    print("STOCK DETAILS:")    
    print("Stock:",stock_N)
    print("Date:",latest['Date'])
    print(f"Open: ₹{latest["Open"]:.2f}")
    print(f"High: ₹{latest["High"]:.2f}")
    print(f"Low: ₹{latest["Low"]:.2f}")
    print(f"Close: ₹{latest["Close"]:.2f}")
    print(f"Volume: {latest["Volume"]:.2f}")
    print(f"Change %: {latest["Change"]:.2f}")
    print()


##########################################################################
#                     SHORT TERM STOCK DETAILS                           #
##########################################################################


def print_short_term_stock(stock_name,period):
    
    """
    Displays short-term stock data and analysis.

    Parameters:
        stock_name (str): Stock symbol
        period (str): Time period (e.g., '3d', '7d', '1mo')

    Returns:
        None
    """

    # Fetch short-term stock data
    stock_N,stock = Get_Short_Term_Stock_Details(stock_name,period)

    # Round numerical values
    stock = stock.round(2)

    # Calculate average stock metrics
    analysis = calculate_stock_average(stock)

    # Add percentage change column
    stock = add_percentage_change(stock)

    # Format currency and percentage columns for display
    stock = format_currency(stock)
    stock = format_change(stock)

    # Generate CSV file name
    today_date = dt.datetime.now().strftime("%Y-%m-%d")
    file_name = f"{stock_N}_{period}_{today_date}.csv"
    
   
    # Display stock data
    print()
    print("Short Term Stock Details:")
    print("Stock Name:",stock_N)
    print("Period:",period)
    print()
    print(tabulate(stock,headers=["Date","Open","High","Low","Close","Volume","Change %"],tablefmt='psql',showindex=False))
    print()

    # Display stock analysis
    print("Stock Analysis:")
    for k,v in analysis.items():
        print(f"{k.replace("_"," ").title()}: ₹{v}")

    # Ask user whether to save the data
    user_inp = input("Do you want to Save this Data (Y/N):").upper()
    if user_inp == "Y":
        stock.to_csv(f"./saved/{file_name}",encoding="utf-8-sig")
        print("Your Data has been saved in 'saved' Folder")



##########################################################################
#                     MULTIPLE STOCK DETAILS                             #
##########################################################################


def print_multiple_stock(stock_names):

    """
    Displays today's stock details for multiple stocks.

    Parameters:
        stock_names (list): List of stock symbols

    Returns:
        None
    """

    # Fetch multiple stock data
    stock = Get_Multiple_Stock_Details(stock_names)

    # Add percentage change
    stock = add_percentage_change(stock)

    # Format currency and percentage values
    display_stock = format_currency(stock)
    display_stock = format_change(display_stock)
    
    # Display stock table
    print("\nMultiple Stock Details:\n")
    print(tabulate(display_stock,headers=["Date","Stock","Open","High","Low","Close","Volume","Change %"], tablefmt='psql',showindex=False))
    print()



##########################################################################
#                     HISTORICAL STOCK DETAILS                           #
##########################################################################


def print_historical_stock(stock,start_date,end_date):

    """
    Displays historical stock data and analysis for a given date range.

    Parameters:
        stock (str): Stock symbol
        start_date (str): Start date (YYYY-MM-DD)
        end_date (str): End date (YYYY-MM-DD)

    Returns:
        None
    """

    # Fetch historical stock data
    stock_name,stock = Get_Historical_Stock_Details(stock,start_date,end_date)
    print("Stock Name:",stock_name)

    # Add percentage change
    stock = add_percentage_change(stock)

    # Calculate stock averages
    analysis = calculate_stock_average(stock)

    # Format currency values for display
    display_stock = format_currency(stock)

    # Display historical stock table
    print("\nHistorical Stock Details\n")
    print(tabulate(
        display_stock,
        headers=["Date","Close","High","Low","Open","Volume","Change %"],
        tablefmt="psql",
        showindex=False
    ))
    
    # Display analysis results
    print()
    print("Stock Analysis:")
    for k,v in analysis.items():
        print(f"{k.replace("_"," ").title()}: ₹{v}")


