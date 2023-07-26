# Collects the information required for pick-up
import time

# List to store user information
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
      print("")
      print("Entry cannot be blank, try again.") # Taken from pizzabot

# Name 
def pickupinfo():
  # Name input
  query = ("Enter your name > ")
  userdetails['name'] = notblank(query)
  # Phone number input
  query = ("Enter your phone number > ")
  userdetails['phone'] = notblank(query)

pickupinfo()

print(userdetails)