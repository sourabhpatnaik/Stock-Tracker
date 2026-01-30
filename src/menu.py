from main import print_today_stock,print_historical_stock

print("1. For Today stock detail")
print("2. For Historical stock detail")
print("3. for Exit\n")

option = int(input("Choose Option:"))
while option != 3:

    if option == 1:
        stock_name = input("Enter Stock Name:")
        print_today_stock(stock_name)
    elif option == 2:
        stock_name = input("Enter Stock Name:")
        period = input("Enter Period (1d/3d/7d/1m/3m):").lower()
        print_historical_stock(stock_name,period)
    
    print("1. For Today stock detail")
    print("2. For Historical stock detail")
    print("3. for Exit")
    option = int(input("Enter:"))