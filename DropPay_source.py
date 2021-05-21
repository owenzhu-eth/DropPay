"""
Book of Resell - DropPay
By OwenZhu78#0001
"""

def DropPay():
    price=float(input("Price of item you want to sell at? "))
    category=str(input("Category of item (electronic,console,media,other)? "))
    shipping=float(input("Estimated shipping cost? "))
    profit=float(input("Profit margin you want to make (enter as decimal)? "))

    if category.lower() == "electronic":
        if price < 101:
            payout=(price-(price*0.08)-shipping-(price*profit))
        elif price > 100:
            payout=(price-(((price-100)*0.08)+15)-shipping-(price*profit))
    elif category.lower() == "console":
        payout=(price-(price*0.08)-shipping-(price*profit))
    elif category.lower() == "media":
        payout=(price-((price*0.08)+1.80)-shipping-(price*profit))
    elif category.lower() == "other":
        payout=(price-(price*0.15)-shipping-(price*profit))

    print(round(payout))

DropPay()
