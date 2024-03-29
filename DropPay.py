"""
EveryFlip Atlanta LLC - DropPay
By Ouwen Zhu
"""
    
print("Enter \"About()\" for more information about this application\nEnter \"Payout()\" to calculate the payout and profit of an item\nEnter \"Advance()\" to calculate the amount of money advanced and held by Payability and out of pocket costs for payouts when using Payability")

def About():
    print("DropPay was developed by Ouwen Zhu, Owner of EveryFlip Atlanta LLC")
    print("DropPay is an application designed to calculate the ideal payout for a dropshipper to provide to their clients")

##def EveryFlipATL():
##    pass

def Payout():
    try:
        price=float(input("Price of item you want to sell at? "))
        category=str(input("Category of item (electronic,media,other)? "))
        shipping=float(input("Estimated shipping cost? "))
        profit=float(input("Profit margin you want to make (enter as a decimal)? "))
        advance=str(input("Using Payability (enter as True or False)? "))

        fee=price*.02
        
        if advance.lower() == "false":
            if category.lower() == "electronic":
                if price < 101:
                    payout=(price-(price*0.08)-shipping-(price*profit))
                elif price > 100:
                    payout=(price-(((price-100)*0.08)+15)-shipping-(price*profit))
            elif category.lower() == "media":
                payout=(price-((price*0.08)+1.80)-shipping-(price*profit))
            elif category.lower() == "other":
                payout=(price-(price*0.15)-shipping-(price*profit))
                            
            if profit >= 1:
                print("Please enter a decimal when prompted")
            elif price < 0 or shipping < 0 or profit < 0:
                print("Please enter non-zero and positive numbers when prompted")
            else:
                print("")
                print("Client payout is " + str(round(payout,2)))
                print("Payability fee is " + str(round(fee,2)))
                print("Profit is " + str(round(price*profit,2)))
        elif advance.lower() == "true":
            if category.lower() == "electronic":
                if price < 101:
                    payout=(price-(price*0.02)-(price*0.08)-shipping-(price*profit))
                elif price > 100:
                    payout=(price-(price*0.02)-(((price-100)*0.08)+15)-shipping-(price*profit))
            elif category.lower() == "media":
                payout=(price-(price*0.02)-((price*0.08)+1.80)-shipping-(price*profit))
            elif category.lower() == "other":
                payout=(price-(price*0.02)-(price*0.15)-shipping-(price*profit))
                        
            if profit >= 1:
                print("Please enter a decimal when prompted")
            elif price < 0 or shipping < 0 or profit < 0:
                print("Please enter non-zero and positive numbers when prompted")
            else:
                print("")
                print("Client payout is " + str(round(payout,2)))
                print("Payability fee is " + str(round(fee,2)))
                print("Profit is " + str(round(price*profit,2)))
        else:
            print("Please enter either True or False when prompted")

    except ValueError:
        print("Please enter a number when prompted")
    except UnboundLocalError:
        print("Please check for typos")

def Advance():
    try:
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
            
        if new_payA == 0 or new_payH == 0 or new_payout==0:
            print("Please check for typos")
        elif price < 0 or shipping < 0 or quantity < 0 or payout < 0:
            print("Please enter non-zero and positive numbers when prompted")
        else:
            print("")
            print("Payability advance is " + str(round(new_payA,2)))
            print("Payability hold is " + str(round(new_payH,2)))
            if payout>payA:
                print("Out of pocket payout is " + str(round(new_payout,2)))
            else:
                print("No out of pocket payout")

    except ValueError:
        print("Please enter a number when prompted")

##def Import():
##    pass
##
##def Export():
##    pass

