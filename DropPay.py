"""
EveryFlip Atlanta - DropPay
By OwenZhu78#0001
"""

def About():
    print("DropPay is a dropshipping payout calculator made by Ouwen Zhu, Owner of EveryFlip Atlanta")

def Payout():
    price=float(input("Price of item you want to sell at? "))
    category=str(input("Category of item (electronic,media,other)? "))
    shipping=float(input("Estimated shipping cost? "))
    profit=float(input("Profit margin you want to make (enter as decimal)? "))
    payA=0
    payH=0
    
    if category.lower() == "electronic":
        if price < 101:
            payout=(price-(price*0.08)-shipping-(price*profit))
        elif price > 100:
            payout=(price-(((price-100)*0.08)+15)-shipping-(price*profit))
    elif category.lower() == "media":
        payout=(price-((price*0.08)+1.80)-shipping-(price*profit))
    elif category.lower() == "other":
        payout=(price-(price*0.15)-shipping-(price*profit))
        
    print("")
    print("Client payout is " + str(round(payout,2)))
    print("Profit is " + str(round(price*profit,2)))


def Advance():
    price=float(input("Price of item you want to sell at? "))
    category=str(input("Category of item (electronic,media,other)? "))
    shipping=float(input("Estimated shipping cost? "))
    quantity=int(input("Quantity sold? "))
    payout=int(input("Payout to client? "))
    payA=0
    payH=0
    new_payA=0
    new_payH=0
    new_payout=0
    
    if category.lower() == "electronic":
        if price < 101:
            payA=(price-(price*0.02)-(price*0.08)-shipping)*0.8
            payH=(price-(price*0.02)-(price*0.08)-shipping)*0.2
        elif price > 100:
            payA=(price-(price*0.02)-(((price-100)*0.08)+15)-shipping)*0.8
            payH=(price-(price*0.02)-(((price-100)*0.08)+15)-shipping)*0.2
    elif category.lower() == "media":
        payA=(price-(price*0.02)-((price*0.08)+1.80)-shipping)*0.8
        payH=(price-(price*0.02)-((price*0.08)+1.80)-shipping)*0.2
    elif category.lower() == "other":
        payA=(price-(price*0.02)-(price*0.15)-shipping)*0.8
        payH=(price-(price*0.02)-(price*0.15)-shipping)*0.2

    new_payA=payA*quantity
    new_payH=payH*quantity
    new_payout=(payout-payA)*quantity
    
    print("")
    print("Payability advance is " + str(round(new_payA,2)))
    print("Payability hold is " + str(round(new_payH,2)))
    if payout>payA:
        print("Out of pocket payout is " + str(round(new_payout,2)))
    else:
        print("No out of pocket payout")
    
