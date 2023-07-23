# Allows user to order for either delivery or click-and-collect
import time

print("Would you like to order for click-and-collect or delivery?")
print("")
print("Enter 1 for Click-and-collect")
print("Enter 2 for Delivery ($9.00 surcharge)")

while True:
    try:
        ordtype = int(input("Enter number here > "))

        if ordtype == 1:
            print("Pick-up!")
            break

        elif ordtype == 2:
            print("Delivery!")
            break

        else:
            print("")
            print("Invalid number! Enter either 1 or 2!")
    
    except ValueError:
        print("")
        print("Invalid input! Please enter either 1 or 2")

# Add connection to userinfo_v* later