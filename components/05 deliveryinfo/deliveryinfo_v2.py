# Collects information required for delivery
import time

# Dictionary to store user information
detail = ['name', 'number', 'house number', 'street', 'suburb']
detaillist = len(detail)

userdetails = {}

# Ensures that inputs cannot be blank
def notblank(query):
    valid = False
    while not valid:
        response = input(query)
        if response != "":
            print("")
            return response
        else:
            print("\nEntry cannot be blank, please try again.") 

# Pick-up info function
def deliveryinfo():
    # General loop for all user inputs
    for count in range (detaillist):
        query = ("Enter your {} > " .format(detail[count]))
        userdetails[detail[count]] = notblank(query)

deliveryinfo()

print(userdetails)