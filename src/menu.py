from main import print_today_stock,print_short_term_stock,print_multiple_stock
from stock_api import Get_Multiple_Stock_Details

print("1. For Today stock detail")
print("2. For Short-Term stock detail")
print("3. For Multiple Stock details")
print("4. for Exit\n")

option = int(input("Choose Option:"))
while option != 4:

    if option == 1:
        stock_name = input("Enter Stock Name:")
        print()
        print_today_stock(stock_name)
    elif option == 2:
        stock_name = input("Enter Stock Name:")
        period = input("Enter Period (1d/3d/7d/1mo/3mo):").lower()
        print_short_term_stock(stock_name,period)
    elif option == 3:
        stocks = list(map(str, input("Enter Stocks (Provide ','):").strip().split(",")))
        print_multiple_stock(stocks)

    print()    
    print("1. For Today stock detail")
    print("2. For Historical stock detail")
    print("3. For Multiple Stock details")
    print("4. for Exit")
    print()
    option = int(input("Enter:"))