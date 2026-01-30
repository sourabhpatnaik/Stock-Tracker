from stock_api import Get_Today_Stock_Detail

# Code to fetch today's Stock details
stock_name = input("Enter Stock Name:").upper()
try:
    if stock_name.__contains__(".NS"):
        Get_Today_Stock_Detail(stock_name)
    else:
        stock_name = stock_name + ".NS"
        Get_Today_Stock_Detail(stock_name)
except:
    print(f"NO DATA FOUND RELATED TO {stock_name}")