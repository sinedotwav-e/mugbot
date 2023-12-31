import random
# Allows for randomly generated variables

from random import randint
# Importing from random to import randint
# It returns a random integer from a range of previously
# specified integers

import time
# Allows the program to delay printing strings to allow for user readability

# List of names for the random name generator
names = ["Doug", "Douglas", "Dougington", "Dougie", "Duggie", "Doogie", "Dougalasa", 
"Dùbhghlas", "Thrangott the Devourer", "Gab", "Doug Doug"]

# Dictionary to store user details
userdetails = {}

# List of relevant details
detail = ['name', 'phone', 'house', 'street', 'suburb']
# Detail list length
detaillist = len(detail)

# Names of mugs
mugnames = ['Plain white mug', 'Plain black mug', 'Plain brown mug', 'Plain green mug', # 1-4 Single tone mugs
            'Striped white & red mug', 'Striped black & yellow mug', 'Gradient magenta & blue mug', 'Gradient black and white mug', # 5-8 Patterned mugs
            'Two-tone green & white mug', 'Two-tone brown & white mug', 'Two-tone blue & purple mug', 'Two-tone black & white mug', # 9-12 Two-toned mugs
            'White skull decal mug', 'Green leaf decal mug', 'Blue sun decal mug', 'Purple gem decal mug', # 13-16 Mugs with a decal
            'Glow-in-the-dark mug', 'Glitter mug', 'Colour changing mug', 'Glass mug', # 17-20 Unique feature mugs
            'Skull shaped mug', 'Wooden tankard', 'Wallace mug (from Wallace & Gromit)', 'Golden, diamond encrusted bowl'] # 21-24 Unique shape mugs

# Prices of mugs
mugprices = [12.50, 12.50, 12.50, 12.50, 14.20, 14.20, 14.20, 14.20, 14.20, 14.20, 14.20, 14.20, # 1-4 Single tone mugs, 5-8 Patterned mugs, 9-12 Two-toned mugs
             16.80, 16.80, 16.80, 16.80, 20.00, 20.00, 20.00, 20.00, 24.00, 24.00, 30.00, 50.00] # 13-16 Mugs with a decal, 17-20 Unique feature mugs, 21-24 Unique shape mugs

mugtotal = 24 # Total number of mugs

# List to stored ordered mugs
orderlist = []
# List to store ordered mugss prices
ordercost = []

# Ensures that inputs cannot be blank in most functions
def notblank(query):
    valid = False
    while not valid:
        response = input(query)
        if response != "":
            print("")
            return response
        else:
            print("\nEntry cannot be blank, please try again.") 

# Welcome screen, does nothing other than make the title look nice
def title():
    title = [
    '███╗   ███╗██╗   ██╗ ██████╗ ███████╗██╗  ██╗ ██████╗ ████████╗██╗',
    '████╗ ████║██║   ██║██╔════╝ ██╔════╝██║  ██║██╔═══██╗╚══██╔══╝██║',
    '██╔████╔██║██║   ██║██║  ███╗███████╗███████║██║   ██║   ██║   ██║',
    '██║╚██╔╝██║██║   ██║██║   ██║╚════██║██╔══██║██║   ██║   ██║   ╚═╝',
    '██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║██║  ██║╚██████╔╝   ██║   ██╗',
    '╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝',
    '',
    '                      By Eardwulf Ulan :p                         '
    ]
    titlelength = len(title)
    for count in range (titlelength):
        print(title[count])
        time.sleep(0.125) 

def exittitle():
    exittitle = [
        ' ██████╗  █████╗  █████╗ ██████╗ ██████╗ ██╗   ██╗███████╗██╗',
        '██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██║',
        '██║  ██╗ ██║  ██║██║  ██║██║  ██║██████╦╝ ╚████╔╝ █████╗  ██║',
        '██║  ╚██╗██║  ██║██║  ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝',
        '╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝   ██║   ███████╗██╗',
        ' ╚═════╝  ╚════╝  ╚════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝',
        ]
    # Gets the number of items in a list
    exitlength = len(exittitle)
    # for loop that prints each item in the list one after the other with a delay for each item in the list
    for count in range (exitlength):
        print(exittitle[count])
        time.sleep(0.125)
    for xt in range (3, 0, -1):
        print(f"Exiting in {xt}...")
        time.sleep(1)
    exit()

# Welcome's user and introduces itself with a randomly generated name
def welcome():
    '''
    Function: To welcome the user with a message and randomly generated name
    Parameters: None
    Returns: None
    '''
    num = randint(1,10)
    name = (names[num])

    print("\nWelcome to MUGSHOT!")
    time.sleep(1.5)
    print("My name is", name, "and I will help you order a brand new mug!")

# Allow user to select what kind of order they would like to place
def ordertype():
    print("Would you like to order for click-and-collect or delivery?")
    time.sleep(1.7)
    print("")
    print("Enter 1 for Click-and-collect")
    print("Enter 2 for Delivery ($9.00 surcharge for 4 or fewer items)")
    print("Enter 0 to exit the program")
    # Ordering options
    while True:
        try:
            ordtype = int(input("Enter number here > "))
            if ordtype == 0:
                exittitle()
            elif ordtype == 1:
                print("\nOrdering for click-and-collect!\n")
                time.sleep(1)
                pickupinfo()
                return "click-and-collect"
            elif ordtype == 2:
                print("\nOrdering for delivery!\n")
                time.sleep(1)
                deliveryinfo()
                return "delivery"
            else:
                print("")
                print("Invalid number! Enter either 1, 2 or 0!")
        except ValueError:
            print("")
            print("Invalid input! Please enter either 1, 2 or 0")

# Collects user information when user selects for pick-up
def pickupinfo():
    # Name input
    for count in range (detaillist - 3):
        query = ("Enter your {} > " .format(detail[count]))
        userdetails[detail[count]] = notblank(query)
    print(userdetails)

# Collects user information when user selects for delivery
def deliveryinfo():
    # General loop for all user inputs
    for count in range (detaillist):
        query = ("Enter your {} > " .format(detail[count]))
        userdetails[detail[count]] = notblank(query)
    print(userdetails)

# Menu that user can select from
def mugmenu():
    print("Here are the mugs you can order from us!") # Menu title
    time.sleep(1.7)
    print("--------------------------------------------------")

    for count in range (mugtotal): # For loop printing the index number, price and item name
        print("{} ${:.2f} {}"  .format(count+1, float(mugprices[count]), mugnames[count])) # Formatted menu
        time.sleep(0.05)

# Allows users to select what they want from the menu provided
def mugordering():
    # Ask for number of mugs required
    mugsnum = 0
# Loop for selecting number of desired mugs
    while True:
        try:
            mugsnum = int(input("\nHow many mugs would you like to order? > "))
            if mugsnum >= 1 and mugsnum <= 20:
                break
            else:
                print("Your order must be between 1 and 20\n")

        except ValueError:
            print ("That is not a valid number")
            print ("Please enter a number between 1 and 20\n")

    print("\nYou are ordering", mugsnum, "mugs.")

    # Loop for selecting desired mugs
    for item in range(mugsnum):
        while mugsnum > 0:
            while True:
                try:
                    mugordered = int(input("By entering the index number on the left, order your mugs > ")) - 1
                    if mugordered >= 0 and mugordered <= 23:
                        break
                    else: 
                        print("\nYour number must be between 1 and 24")
                        
                except ValueError:
                        print ("\nThat is not a valid number")
                        print ("Please enter number enter between 1 and 24\n")
                        
            orderlist.append(mugnames[mugordered])
            ordercost.append(mugprices[mugordered])
            print("\n!! You have ordered a ${:.2f} {} !!" .format(mugprices[mugordered], mugnames[mugordered]))
            mugsnum = mugsnum - 1
            print("\n ", mugsnum, "mugs remaining")

# Prints order and user information
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

# Allow user to create another order or exit the program
def neworexit():
    # Basic user instructions
    print("Would you like to order again or exit the program?")
    print("Enter 1 to exit program")
    print("Enter 2 to restart program")
    # While loop to avoid crashing
    while True:
        try:
            # Integer input for exit or restart
            newexit = int(input("Enter number here > "))
            if newexit == 1: # Exit option
                exittitle()
            elif newexit == 2: # Restart option
                userdetails.clear()
                orderlist.clear()
                ordercost.clear()
                print("Restarting...\n")
                time.sleep(1)
                main()
                break
            else:# Invalid integer entered
                print("")
                print("Invalid number! Enter either 1 or 2!")
        except ValueError: # Invalid value intered
                print("")
                print("Invalid input! Please enter either 1 or 2!")

# Main function, runs all other functions
def main():
    '''
    Function: To run all other functions
    Parameters: None
    Returns: None
    '''
    title()
    time.sleep(2.7)
    welcome()
    time.sleep(1.8)
    deliverypickup = ordertype()
    mugmenu()
    mugordering()
    receipt(deliverypickup)
    neworexit()

main()