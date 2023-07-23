import random
from random import randint
import time

# List of names for the random name generator
names = ["Doug", "Douglas", "Dougington", "Dougie", "Duggie", "Doogie", "Dougalasa", 
"Dùbhghlas", "Thrangott the Devourer", "Gab", "Doug Doug"]

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

# Welcome's user and introduces itself with a randomly generated name
def welcome():
    num = randint(1,10)
    name = (names[num])

    print("Welcome to MUGSHOT!")
    time.sleep(1.5)
    print("My name is", name, "and I will help you order a brand new mug!")
    time.sleep(1.8)

def ordertype():
    


# Main function, runs all other functions
def main():
    '''
    Function: To run all other functions
    Parameters: None
    Returns: None
    '''
    title()
    welcome()

main()