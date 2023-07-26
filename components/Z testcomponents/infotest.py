userdetails = {}

detail = ['name', 'phone number', 'house number', 'street name', 'suburb']
detaillist = len(detail)

# function for blank inputs
def notblank(query):
  valid = False
  while not valid:
    response = input(query)

    if response != "":
      print("")
      return response
  
    else:
      print("")
      print("Entry cannot be blank, try again.")

def delinfo():
  for count in range (detaillist):
    if count == 1:
      while True:
            try:
                query = ("Please enter your {} > " .format(detail[count]))
                userdetails[detail[count]] = notblank(query)
                break
            except ValueError:
               print("Invalid input")

    else:
      query = ("Please enter your {} > " .format(detail[count]))
      userdetails[detail[count]] = notblank(query)

delinfo()

print(userdetails[detail[1]])

# experimental delinfo function using a list instead of repeating the line of code 5 times