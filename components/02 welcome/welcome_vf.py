# Welcomes the user, and bot introduces itself with a randomly generated name
import random
from random import randint
import time

# List of names
names = ["Doug", "Douglas", "Dougington", "Dougie", "Duggie", "Doogie", "Dougalasa", 
"Dùbhghlas", "Thrangott the Devourer", "Gab", "Doug Doug"]

def welcome():
    # Random number generator
    num = randint(1,10)
    name = (names[num])

    # Welcome message with random name
    print("Welcome to MUGSHOT!")
    time.sleep(1.5)
    print("My name is", name, "and I will help you order a brand new mug!")
    time.sleep(1.8)

welcome()