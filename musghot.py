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
detail = ['name', 'number', 'house number', 'street', 'suburb']
# Detail list length
detaillist = len(detail)

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
    time.sleep(2.7)

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
    time.sleep(1.8)

def ordertype():
    deiverypickup = 0
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
                print("Goodbye~!")
                time.sleep(3) # Replace with program exit function
                exit()
            elif ordtype == 1:
                print("\nOrdering for click-and-collect!\n")
                time.sleep(1)
                deiverypickup = "click-and-collect"
                pickupinfo()
                break
            elif ordtype == 2:
                print("\nOrdering for delivery!\n")
                time.sleep(1)
                deiverypickup = "delivery"
                deliveryinfo()
                break
            else:
                print("")
                print("Invalid number! Enter either 1, 2 or 0!")
        except ValueError:
            print("")
            print("Invalid input! Please enter either 1, 2 or 0")

# Collects user information when user selects for pick-up
def pickupinfo():
    # Name input
    query = ("Enter your name > ")
    userdetails['name'] = notblank(query)
    # Phone number input
    query = ("Enter your phone number > ")
    userdetails['phone'] = notblank(query)
    print(userdetails)

# Collects user information when user selects for delivery
def deliveryinfo():
    # General loop for all user inputs
    for count in range (detaillist):
        query = ("Enter your {} > " .format(detail[count]))
        userdetails[detail[count]] = notblank(query)

# Main function, runs all other functions
def main():
    '''
    Function: To run all other functions
    Parameters: None
    Returns: None
    '''
    #title()
    #welcome()
    ordertype()

main()