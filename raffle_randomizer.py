"""
Book of Resell - DropPay
By OwenZhu78#0001
"""

def DropPay():
    price_in=float(input("Price of item you want to sell at? "))
    category_in=str(input("Category of item (electronic,console,media,other)? "))
    shipping_in=int(input("Estimated shipping cost? "))
    profit_in=float(input("Profit margin you want to make (enter as decimal)? "))

    if category_in.lower() == "electronic":
        if price_in < 101:
            payout=(price_in-(price_in*0.08)-shipping_in-(price_in*profit_in))
        elif price_in > 100:
            payout=(price_in-(((price_in-100)*0.08)+15)-shipping_in-(price_in*profit_in))
    #elif category_in.lower() == "console":
        ###
    #elif category_in.lower() == "media":
        ###
    #elif category_in.lower() == "other":
        ###

    print(payout)

DropPay()

