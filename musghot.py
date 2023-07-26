import random
from random import randint
import time

# List of names for the random name generator
names = ["Doug", "Douglas", "Dougington", "Dougie", "Duggie", "Doogie", "Dougalasa", 
"Dùbhghlas", "Thrangott the Devourer", "Gab", "Doug Doug"]

# Dictionary to store user details
userdetails = {}

# Ensures that inputs cannot be blank in most functions
def notblank(query):
  valid = False
  while not valid:
    response = input(query)
    if response != "":
      print("")
      return response
    else:
      print("")
      print("Entry cannot be blank, try again.") # Taken from pizzabot

# Welcome screen, does nothing other than make the title look nice
def title():
    '''
    Function: To make the program aesthecially pleasing
    Parameters: None
    Returns: None
    '''
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
    num = randint(1,10)
    name = (names[num])

    print("\nWelcome to MUGSHOT!")
    time.sleep(1.5)
    print("My name is", name, "and I will help you order a brand new mug!")
    time.sleep(1.8)

def ordertype():
    deiverypickup = 0
    print("Would you like to order for click-and-collect or delivery?")
    time.sleep(2.5)
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
                print("Ordering for click-and-collect!")
                deiverypickup = "click-and-collect"
                pickupinfo()
                break
            elif ordtype == 2:
                print("Delivery!") # Replace with deliveryinfo_v*
                deiverypickup = "delivery"
                break
            else:
                print("")
                print("Invalid number! Enter either 1 or 2!")
        except ValueError:
            print("")
            print("Invalid input! Please enter either 1 or 2")

# Collects user information when user selects for pick-up
def pickupinfo():
  # Name input
  query = ("Enter your name > ")
  userdetails['name'] = notblank(query)
  # Phone number input
  query = ("Enter your phone number > ")
  userdetails['phone'] = notblank(query)


# Main function, runs all other functions
def main():
    '''
    Function: To run all other functions
    Parameters: None
    Returns: None
    '''
    title()
    welcome()
    ordertype()

main()