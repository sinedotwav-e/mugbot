# Allows users to select what they want from the menu provided

# Names of mugs
mugnames = ['Plain white mug', 'Plain black mug', 'Plain brown mug', 'Plain green mug', # 1-4 Single tone mugs
            'Striped white & red mug', 'Striped black & yellow mug', 'Gradient magenta & blue mug', 'Gradient black and white mug', # 5-8 Patterned mugs
            'Two-tone green & white mug', 'Two-tone brown & white mug', 'Two-tone blue & purple mug', 'Two-tone black & white mug', # 9-12 Two-toned mugs
            'White skull decal mug', 'Green leaf decal mug', 'Blue sun decal mug', 'Purple gem decal mug', # 13-16 Mugs with a decal
            'Glow-in-the-dark mug', 'Glitter mug', 'Colour changing mug', 'Glass mug', # 17-20 Unique feature mugs
            'Skull shaped mug', 'Wooden tankard', 'Wallace mug (from Wallace & Gromit)', 'Golden, diamond encrusted bowl'] # 21-24 Unique shape mugs

# Prices of mugs
mugprices = [12.50, 12.50, 12.50, 12.50, 14.20, 14.20, 14.20, 14.20, 14.20, 14.20, 14.20, 14.20, # 1-4 Single tone mugs, 5-8 Patterned mugs, 9-12 Two-toned mugs
             16.80, 16.80, 16.80, 16.80, 20.00, 20.00, 20.00, 20.00, 24.00, 24.00, 30.00, 50.00] # 13-16 Mugs with a decal, 17-20 Unique feature mugs, 21-24 Unique shap

mugtotal = 24 # Total number of mugs

def mugmenu():
    print("Select your mugs from the list below!\n-----------------------------------------") # Menu title

    for count in range (mugtotal): # For loop printing the index number, price and item name
        print("{} ${:.2f} {}"  .format(count+1, float(mugprices[count]), mugnames[count])) # Formatted menu
    print()

mugmenu()

# List to stored ordered mugs
orderlist = []
# List to store ordered mugss prices
ordercost = []

# Ask for number of mugs required
mugsnum = 0

mugsnum = int(input("How many mugs would you like to order? > "))

print("You are ordering", mugsnum, "mugs.")

print("Please select your mugs by entering the number on the left of the menu")
for item in range(mugsnum):
    while mugsnum > 0:
        mugordered = int(input()) - 1 # Starts at 0, so to match index number, -1
        orderlist.append(mugnames[mugordered])
        ordercost.append(mugprices[mugordered])
        print("You have ordered a ${:.2f} {}" .format(mugprices[mugordered], mugnames[mugordered]))
        mugsnum = mugsnum - 1
        print("\n", mugsnum, "mugs remaining")

print(orderlist)
print(ordercost)