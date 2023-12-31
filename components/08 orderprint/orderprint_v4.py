# Gives the user the collected information and how much their order costs
import time

# Dictionary of stored user details
userdetails = {'name':'Earf', 'phone':'123456789', 'house':'24', 'street':'Manapouri Pl', 'suburb':'Pakuranga'} # Placeholder details
# List to stored ordered mugs
orderlist = ['Plain white mug', 'Glow-in-the-dark mug'] # Placeholder items
# List to store ordered mugss prices
ordercost = [12.60, 20.00] # Placeholder prices

def placeholder(deliverypickup):
    deiverypickup = input("enter 'delivery' or not ")
    return deliverypickup

def placeholder2(mugsnum):
    mugsnum = int(input("enter a number "))
    return mugsnum

def receipt(deliverypickup, mugsnum):
    deliverypickup = placeholder(deliverypickup)
    mugsnum = placeholder2(mugsnum)
    totalcost = sum(ordercost)

    print("\nName: {}\nPhone Number: {}\nHouse Number: {}\nStreet Name: {}\nSuburb: {}\n"
        .format(userdetails['name'], userdetails['phone'], userdetails['house'], userdetails['street'], userdetails['suburb']))

    time.sleep(3)

    count = 0
    for item in orderlist:
        print("Ordered: {} | Cost: ${:.2f}" .format(item, ordercost[count]))
        count = count + 1

    time.sleep(3)

    print()
    if deliverypickup == "delivery" and mugsnum < 5:
        ordercost.append(9.00)
        print("+$9.00 delivery (Less than 5 items ordered)")
    elif deliverypickup == "delivery" and mugsnum > 4:
        print("+$0.00 delivery (5 or more items ordered)")
    else:
        print("+$0.00 delivery (click-and-collect selected)")

    time.sleep(2.4)
    print()

    print("Total Order Cost w/ Delivery:", f"${totalcost:.2f}")

placeholder(deliverypickup)
placeholder2(mugsnum)
receipt()

# VERY BROKEN