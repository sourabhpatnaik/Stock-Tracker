from stock_api import Get_Today_Stock_Detail,Get_Short_Term_Stock_Details,Get_Multiple_Stock_Details,Get_Historical_Stock_Details
from analysis import add_percentage_change,calculate_stock_average
from formatter import format_currency,format_change
from tabulate import tabulate
import datetime as dt

# Code to fetch today's Stock details
def print_today_stock(stock_name):

    stock_N,stock_data = Get_Today_Stock_Detail(stock_name)
    stock_data = stock_data.drop(columns=["Dividends","Stock Splits"])
    stock_data = stock_data.reset_index()
    stock_data["Date"] = stock_data["Date"].dt.date
    stock_data = add_percentage_change(stock_data)
    latest = stock_data.iloc[-1]
    
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


# Code to fetch Historical Stock Data
def print_short_term_stock(stock_name,period):
    
    stock_N,stock = Get_Short_Term_Stock_Details(stock_name,period)
    stock = stock.round(2)
    analysis = calculate_stock_average(stock)
    stock = add_percentage_change(stock)
    stock = format_currency(stock)
    stock = format_change(stock)
    today_date = dt.datetime.now().strftime("%Y-%m-%d")
    file_name = f"{stock_N}_{period}_{today_date}.csv"
    
   
    
    print()
    print("Short Term Stock Details:")
    print("Stock Name:",stock_N)
    print("Period:",period)
    print()
    print(tabulate(stock,headers=["Date","Open","High","Low","Close","Volume","Change %"],tablefmt='psql',showindex=False))
    print()

    print("Stock Analysis:")
    
    for k,v in analysis.items():
        print(f"{k.replace("_"," ").title()}: ₹{v}")



    user_inp = input("Do you want to Save this Data (Y/N):").upper()
    if user_inp == "Y":
        stock.to_csv(f"./saved/{file_name}",encoding="utf-8-sig")
        print("Your Data has been saved in 'saved' Folder")




# Code to fetch multiple stock Data (Only for Today) 
def print_multiple_stock(stock_names):

    stock = Get_Multiple_Stock_Details(stock_names)
    stock = add_percentage_change(stock)
    display_stock = format_currency(stock)
    display_stock = format_change(display_stock)
    
    print("\nMultiple Stock Details:\n")
    print(tabulate(display_stock,headers=["Date","Stock","Open","High","Low","Close","Volume","Change %"], tablefmt='psql',showindex=False))
    print()



# Code to Fetch Historical Data 
def print_historical_stock(stock,start_date,end_date):

    stock_name,stock = Get_Historical_Stock_Details(stock,start_date,end_date)
    print("Stock Name:",stock_name)
    stock = add_percentage_change(stock)
    analysis = calculate_stock_average(stock)
    display_stock = format_currency(stock)

    print("\nHistorical Stock Details\n")
    print(tabulate(
        display_stock,
        headers=["Date","Close","High","Low","Open","Volume","Change %"],
        tablefmt="psql",
        showindex=False
    ))
    
    print()
    print("Stock Analysis:")
    for k,v in analysis.items():
        print(f"{k.replace("_"," ").title()}: ₹{v}")

