# Collects information required for pick-up
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
def pickupinfo():
    # Name input:
    query = ("Enter your name > ")
    userdetails['name'] = notblank(query)
    # Phone number input
    query = ("Enter your phone number > ")
    userdetails['phone'] = notblank(query)
    
pickupinfo()

print(userdetails)