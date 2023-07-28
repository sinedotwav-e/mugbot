# Allow user to create another order or exit the program
import time

# Placeholder details
# User details
userdetails = {'name':'Earf', 'phone':123456789}
# List to stored ordered mugs
orderlist = ['White mug', 'Black mug']
# List to store ordered mugss prices
ordercost = [12.20, 12.20]

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
                print("Goodbye!~")
                time.sleep(3)
                exit()
            elif newexit == 2: # Restart option
                userdetails.clear()
                orderlist.clear()
                ordercost.clear()
                print("Restarting...")
                time.sleep(1)
                main()
                break
            else:# Invalid integer entered
                print("")
                print("Invalid number! Enter either 1 or 2!")
        except ValueError: # Invalid value intered
                print("")
                print("Invalid input! Please enter either 1 or 2!")

# Placeholder main function
def main():
     print("Restarting!!!")
     print(userdetails, ordercost, orderlist)

neworexit()