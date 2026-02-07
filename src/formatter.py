# ADDING RUPEE SIGN TO ["Open","High","Low","Close"] columns

def format_currency(stock_data):
    stock = stock_data.copy()

    for col in ["Open","High","Low","Close"]:
        stock[col] = stock[col].apply(lambda x: f"₹{round(x,2)}")
    return stock

def format_change(stock_data):
    stock = stock_data.copy()

    for col in ["Change %"]:
        stock[col] = stock[col].apply(lambda x: f"{round(x,2)} %")
    return stock