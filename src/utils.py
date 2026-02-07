# FIXING OUR STOCK NAME IF IT CONTAINS '.NS' THEN ALL GOOD OTHER WISE WE ATTACH '.NS' TO OUR STOCK NAME

def normalize_stock(stock):
    stock = stock.strip().upper()
    if not stock.endswith(".NS"):
        stock = stock + ".NS"
    return stock


def normalize_multiple_stock(stock_list):
    new_stock_list = []
    for stock in stock_list:
        stock = stock.strip().upper()
        if not stock.endswith(".NS"):
            stock += ".NS"
            new_stock_list.append(stock)
        else:
            new_stock_list.append(stock)
    return new_stock_list