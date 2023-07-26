# Final copy (changes can be made later)
# Allows user to order for either delivery or click-and-collect
import time

def ordertype():
    deiverypickup = 0
    print("Would you like to order for click-and-collect or delivery?")
    time.sleep(2.5)
    print("")
    print("Enter 1 for Click-and-collect")
    print("Enter 2 for Delivery ($9.00 surcharge)")
    print("Enter 0 to exit the program")

    while True:
        try:
            ordtype = int(input("Enter number here > "))
            if ordtype == 0:
                print("Goodbye~!")
                time.sleep(3) # Replace with program exit function
                exit()
            elif ordtype == 1:
                print("Pick-up!") # Replace with pickupinfo_v*
                deiverypickup = "click-and-collect"
                break
            elif ordtype == 2:
                print("Delivery!") # Replace with deliveryinfo_v*
                deiverypickup = "delivery"
                break
            else:
                print("")
                print("Invalid number! Enter either 1, 2 or 0!")
        except ValueError:
            print("")
            print("Invalid input! Please enter either 1, 2 or 0!")

ordertype()