# Collects information required for delivery
import time

# Dictionary to store user information
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
    # Name input:
    query = ("Enter your name > ")
    userdetails['name'] = notblank(query)
    # Phone number input
    query = ("Enter your phone number > ")
    userdetails['phone'] = notblank(query)
    # House number input
    query = ("Enter your house number > ")
    userdetails['house number'] = notblank(query)
    # Street name input
    query = ("Enter your street > ")
    userdetails['street'] = notblank(query)
    # Suburb name input
    query = ("Enter your suburb > ")
    userdetails['suburb'] = notblank(query)

deliveryinfo()

print(userdetails)