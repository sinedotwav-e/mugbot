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

while True:
    try:
        newexit = int(input("Enter number here > "))
        if newexit == 1:
            print("Goodbye!~")
            time.sleep(3)
            exit()
        
        elif newexit == 2:
            print("Restarting...")
            time.sleep(3)
            main()
            break

        else:
            print("")
            print("Invalid number! Enter either 1 or 2!")

    except ValueError:
            print("")
            print("Invalid input! Please enter either 1 or 2!")