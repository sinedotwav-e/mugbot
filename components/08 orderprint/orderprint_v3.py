# Gives the user the collected information and how much their order costs

deiverypickup = input()
mugsnum = 5

# Dictionary of stored user details
userdetails = {'name':'Earf', 'phone':'123456789', 'house':'24', 'street':'Manapouri Pl', 'suburb':'Pakuranga'} # Placeholder details
# List to stored ordered mugs
orderlist = ['Plain white mug', 'Glow-in-the-dark mug'] # Placeholder items
# List to store ordered mugss prices
ordercost = [12.60, 20.00] # Placeholder prices

print("\nName: {}\nPhone Number: {}\nHouse Number: {}\nStreet Name: {}\nSuburb: {}\n"
      .format(userdetails['name'], userdetails['phone'], userdetails['house'], userdetails['street'], userdetails['suburb']))

count = 0
for item in orderlist:
    print("Ordered: {} | Cost: ${:.2f}" .format(item, ordercost[count]))
    count = count + 1

print()
if deiverypickup == "delivery" and mugsnum > 4:
    ordercost.append(9.00)
    print("$9.00 delivery")
elif deiverypickup == "delivery" and mugsnum > 5:
    print("$0.00 delivery (5 or more items ordered)")

totalcost = sum(ordercost)

print("Total order cost")
print(f"${totalcost:.2f}")