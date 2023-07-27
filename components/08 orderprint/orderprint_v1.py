# Gives the user the collected information and how much their order costs

# List to stored ordered mugs
orderlist = ['Plain white mug', 'Plain black mug'] # Placeholder items
# List to store ordered mugss prices
ordercost = [12.60, 12.60] # Placeholder prices

count = 0
for item in orderlist:
    print("Ordered: {}\nCost: ${:.2f}" .format(item, ordercost[count]))
    count = count + 1