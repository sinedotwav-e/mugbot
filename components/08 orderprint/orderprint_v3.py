# Gives the user the collected information and how much their order costs

# Dictionary of stored user details
userdetails = {'name':'Earf', 'phone':'123456789', 'house':'24', 'street':'Manapouri Pl', 'suburb':'Pakuranga'} # Placeholder details
# List to stored ordered mugs
orderlist = ['Plain white mug', 'Glow-in-the-dark mug'] # Placeholder items
# List to store ordered mugss prices
ordercost = [12.60, 20.00] # Placeholder prices

totalcost = sum(ordercost)

print("\nName: {}\nPhone Number: {}\nHouse Number: {}\nStreet Name: {}\nSuburb: {}\n"
      .format(userdetails['name'], userdetails['phone'], userdetails['house'], userdetails['street'], userdetails['suburb']))

count = 0
for item in orderlist:
    print("Ordered: {} | Cost: ${:.2f}" .format(item, ordercost[count]))
    count = count + 1

print("\nTotal order cost")
print(f"${totalcost:.2f}")