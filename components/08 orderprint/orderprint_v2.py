# Gives the user the collected information and how much their order costs

# Dictionary of stored user details
userdetails = {'name':'Earf', 'phone':'123456789', 'house':'24', 'street':'Manapouri Pl', 'suburb':'Pakuranga'}
# List to stored ordered mugs
orderlist = ['Plain white mug', 'Plain black mug'] # Placeholder items
# List to store ordered mugss prices
ordercost = [12.60, 12.60] # Placeholder prices

print("\nName: {}\nPhone Number: {}\nHouse Number: {}\nStreet Name: {}\nSuburb: {}\n"
      .format(userdetails['name'], userdetails['phone'], userdetails['house'], userdetails['street'], userdetails['suburb']))

count = 0
for item in orderlist:
    print("Ordered: {}\nCost: ${:.2f}" .format(item, ordercost[count]))
    count = count + 1