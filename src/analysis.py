# FUNCTION TO IMPLEMENT STOCK PERCENTAGE CHANGE
def add_percentage_change(stock_data):
    stock = stock_data.copy()

    stock["Change %"] = ((stock["Close"] - stock["Open"]) / stock["Open"] ) * 100
    stock["Change %"] = stock["Change %"].round(2)
    return stock

# FUNCTION TO CALCULATE STOCK AVERAGE VALUES
def calculate_stock_average(stock):
    return {
        "avg_open" : round(stock["Open"].mean(),2),
        "avg_high" : round(stock["High"].mean(),2),
        "avg_low" : round(stock["Low"].mean(),2),
        "avg_close" : round(stock["Close"].mean(),2)
    }