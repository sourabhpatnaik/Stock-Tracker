import yfinance as yfc
import pandas as pd
from utils import normalize_stock,normalize_multiple_stock


##########################################################################
#                     TODAY's STOCK DETAILS                           #       
##########################################################################

def Get_Today_Stock_Detail(stock):

    stock = normalize_stock(stock)
    # Getting the Stock from yfinance
    stock_name = yfc.Ticker(stock)
    # Storing the data 
    stock_data = stock_name.history(period="1d")
    return stock,stock_data

##########################################################################
#                     SHORT TERM STOCK DETAILS                           #       
##########################################################################


def Get_Short_Term_Stock_Details(stock,period):
         
    stock = normalize_stock(stock)
    # taking stock name 
    stock_name = yfc.Ticker(stock)
    
    # Getting the stock data    
    stock_data = stock_name.history(period=period)
    
    # Removing unnecessay columns for dataframe
    stock_data.drop(["Dividends","Stock Splits"],axis="columns",inplace=True)
    
    stock_data = stock_data.reset_index()
    stock_data["Date"] = stock_data["Date"].dt.date 
    return stock,stock_data


##########################################################################
#                     MULTIPLE STOCK DETAILS                           #       
##########################################################################

def Get_Multiple_Stock_Details(stock_list):
    stock_list = normalize_multiple_stock(stock_list)
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
    return final_stock 



##########################################################################
#                     HISTORICAL STOCK DETAILS                           #       
##########################################################################


def Get_Historical_Stock_Details(stock,start_date,end_date):

    stock = normalize_stock(stock)

    stock_data = yfc.download(stock,start=start_date,end=end_date)
    stock_data.columns = stock_data.columns.droplevel(1)
    stock_data.columns.name = None
    stock_data = stock_data.reset_index()
    stock_data["Date"] = stock_data["Date"].dt.date
    return stock,stock_data
