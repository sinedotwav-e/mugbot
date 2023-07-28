import time

userdetails = {}

deiverypickup = input("Delivery? (type, 'delivery') ")
mugsnum = 5

# Dictionary of stored user details
userdetails = {'name':'Earf', 'phone':'123456789', 'house':'24', 'street':'Manapouri Pl', 'suburb':'Pakuranga'} # Placeholder details
# List to stored ordered mugs
orderlist = ['Plain white mug', 'Glow-in-the-dark mug'] # Placeholder items
# List to store ordered mugss prices
ordercost = [12.60, 20.00] # Placeholder prices

def receipt(deliverypickup):
    if len(userdetails) == 2:
        print("\nName: {}\nPhone Number: {}\n"
        .format(userdetails['name'], userdetails['phone']))
    elif len(userdetails) == 5:
        print("\nName: {}\nPhone Number: {}\nHouse Number: {}\nStreet Name: {}\nSuburb: {}\n"
        .format(userdetails['name'], userdetails['phone'], userdetails['house'], userdetails['street'], userdetails['suburb']))
    time.sleep(3)
    count = 0
    for item in orderlist:
        print("Cost: ${:.2f} | Ordered: {}" .format(ordercost[count], item))
        count = count + 1
    time.sleep(len(orderlist)*0.2+2)
    print()
    if deliverypickup == "delivery" and len(orderlist) < 5:
        ordercost.append(9.00)
        print("+$9.00 delivery (Less than 5 items ordered)")
    elif deliverypickup == "delivery" and len(orderlist) > 5:
        print("+$0.00 delivery (5 or more items ordered)")
    else:
        print("+$0.00 delivery (click-and-collect selected)")
    totalcost = sum(ordercost)
    time.sleep(1.5)
    print("\n--------------------------------------------------")
    print("Total Order Cost w/ Delivery:", f"${totalcost:.2f}")
    print("--------------------------------------------------")