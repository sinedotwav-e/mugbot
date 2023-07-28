# Allow user to create another order or exit the program
import time

userdetails = {'name':'Earf', 'phone':123456789}
# List to stored ordered mugs
orderlist = ['White mug', 'Black mug']
# List to store ordered mugss prices
ordercost = [12.20, 12.20]

# Basic user instructions
print("Would you like to order again or exit the program?")
print("Enter 1 to exit program")
print("Enter 2 to restart program")

# Placeholder main function
def main():
     print("Restarting!!!")
     print(userdetails, ordercost, orderlist)

# While loop to avoid crashing
while True:
    try:
        # Integer input for exit or restart
        newexit = int(input("Enter number here > "))
        # Exit option
        if newexit == 1:
            print("Goodbye!~")
            time.sleep(3)
            exit()
        
        # Restart option
        elif newexit == 2:
            print("Goodbye!~")
            time.sleep(3)
            userdetails.clear()
            orderlist.clear()
            ordercost.clear()
            main()
            break
        
        # Invalid integer entered
        else:
            print("")
            print("Invalid number! Enter either 1 or 2!")

    # Invalid value intered
    except ValueError:
            print("")
            print("Invalid input! Please enter either 1 or 2!")