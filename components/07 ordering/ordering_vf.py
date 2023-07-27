# Allows users to select what they want from the menu provided

# List to stored ordered mugs
orderlist = []
# List to store ordered mugss prices
ordercost = []

def mugordering():
    # Ask for number of mugs required
    mugsnum = 0

# Loop for selecting number of desired mugs
    while True:
        try:
            mugsnum = int(input("How many mugs would you like to order? > "))
            if mugsnum >= 1 and mugsnum <= 20:
                break
            else:
                print("\nYour order must be between 1 and 20")

        except ValueError:
            print ("\nThat is not a valid number")
            print ("Please enter a number between 1 and 20")

    print("\nYou are ordering", mugsnum, "mugs.\n")

    # Loop for selecting desired mugs
    for item in range(mugsnum):
        while mugsnum > 0:
            while True:
                try:
                    mugordered = int(input("By entering the index number on the left, order your mugs > "))
                    if mugordered >= 1 and mugordered <= 24:
                        break
                    else: 
                        print("Your number must be between 1 and 24")
                        
                except ValueError:
                        print ("That is not a valid number")
                        print ("Please enter number enter between 1 and 24 ")
                        
            orderlist.append(mugnames[mugordered])
            ordercost.append(mugprices[mugordered])
            print("You have ordered a ${:.2f} {}" .format(mugprices[mugordered], mugnames[mugordered]))
            mugsnum = mugsnum - 1
            print("\n", mugsnum, "mugs remaining")

print(orderlist)
print(ordercost)