# Gives the user the collected information and how much their order costs

import time

deiverypickup = input("enter 'delivery' or not")
mugsnum = int(input("enter a number"))

# Dictionary of stored user details
userdetails = {'name':'Earf', 'phone':'123456789', 'house':'24', 'street':'Manapouri Pl', 'suburb':'Pakuranga'} # Placeholder details
# List to stored ordered mugs
orderlist = ['Plain white mug', 'Glow-in-the-dark mug'] # Placeholder items
# List to store ordered mugss prices
ordercost = [12.60, 20.00] # Placeholder prices

totalcost = sum(ordercost)

print("\nName: {}\nPhone Number: {}\nHouse Number: {}\nStreet Name: {}\nSuburb: {}\n"
      .format(userdetails['name'], userdetails['phone'], userdetails['house'], userdetails['street'], userdetails['suburb']))

time.sleep(2)

count = 0
for item in orderlist:
    print("Ordered: {} | Cost: ${:.2f}" .format(item, ordercost[count]))
    count = count + 1

time.sleep(2)

print()
if deiverypickup == "delivery" and mugsnum < 5:
    ordercost.append(9.00)
    print("+$9.00 delivery (Less than 5 items ordered)")
elif deiverypickup == "delivery" and mugsnum > 4:
    print("+$0.00 delivery (5 or more items ordered)")
else:
    print("+$0.00 delivery (click-and-collect selected)")

time.sleep(2)
print()

print("Total Order Cost w/ Delivery:", f"${totalcost:.2f}")