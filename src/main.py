from stock_api import Get_Today_Stock_Detail,Get_Historical_Stock_Details
import pandas as pd

# Code to fetch today's Stock details
def print_today_stock(stock_name):
    try:
        if stock_name.__contains__(".NS"):
            Get_Today_Stock_Detail(stock_name)
        else:
            stock_name = stock_name + ".NS"
            Get_Today_Stock_Detail(stock_name)
    except:
        print(f"NO DATA FOUND RELATED TO {stock_name}")

# Code to fetch Historical Stock Data
def print_historical_stock(stock_name,period):
    try:
        if stock_name.__contains__(".NS"):
            Get_Historical_Stock_Details(stock_name,period)
        else:
            stock_name = stock_name + ".NS"
            Get_Historical_Stock_Details(stock_name,period)
    except:
        print(f"NO DATA FOUND RELATED TO {stock_name} or {period}")

