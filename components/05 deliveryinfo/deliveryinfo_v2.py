# Collects information required for delivery
import time

# Dictionary to store user information
userdetails = {}

detail = ['name', 'phone', 'house number', 'street', 'suburb']
detaillist = len(detail)

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
    for count in range (detaillist):
        # Generalized input for all entries
        query = ("Enter your {} > " .format(detail[count]))
        userdetails[detail[count]] = notblank(query)

deliveryinfo()

print(userdetails)