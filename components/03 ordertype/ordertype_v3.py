# Allows user to order for either delivery or click-and-collect
import time

# Instructions for user
print("Would you like to order for click-and-collect or delivery?")
time.sleep(2.5)
print("")
print("Enter 1 for Click-and-collect")
print("Enter 2 for Delivery ($9.00 surcharge)")
print("Enter 0 to exit the program")

while True:
    try:
        # User input
        ordtype = int(input("Enter number here > "))

        # Allows user to exit program early
        if ordtype == 0:
            print("Goodbye~!")
            time.sleep(3) # Replace with program exit function
            exit()

        # Selects for pick-up
        elif ordtype == 1:
            print("Pick-up!") # Replace with pickupinfo_v*
            break

        # Selects for delivery
        elif ordtype == 2:
            print("Delivery!") # Replace with deliveryinfo_v*
            break
        
        # Prevents numbers other than valid ones from being entered
        else:
            print("")
            print("Invalid number! Enter either 1, 2 or 0!")
    
    # Prevents any other inputs than valid ones from being entered
    except ValueError:
        print("")
        print("Invalid input! Please enter either 1, 2 or 0!")

# Add connection to userinfo later