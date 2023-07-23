# Allows user to order for either delivery or click-and-collect
import time

print("Would you like to order for click-and-collect or delivery?")
print("")
print("Enter 1 for Click-and-collect")
print("Enter 2 for Delivery ($9.00 surcharge)")

ordtype = int(input("Enter number here > "))

if ordtype == 1:
    print("Pick-up!")

elif ordtype == 2:
    print("Delivery!")

else:
    print("Invalid input! Try again!")