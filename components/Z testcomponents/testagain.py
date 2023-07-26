userdetails = {}
detail = ['name', 'phone number', 'house number', 'street name', 'suburb']

def notvalid(query, integercheck = False):
    while True:
        response = input(query)
        if response.strip():
            if integercheck:
                try:
                    return int(response)
                except ValueError:
                    print("Invalid input. Please enter a valid number")
            else:
                return response
        else:
            print("Entry cannot be blank. Try again.")

def delinfo():
    for item in detail:
        integercheck = item == 'phone number'
        query = ("Please enter your {} > ".format(item))
        userdetails[item] = notvalid(query, integercheck)

delinfo()

print(userdetails['phone number'])

print("\nUser Details:")
for key, value in userdetails.items():
    print(f"{key.title()}: {value}")