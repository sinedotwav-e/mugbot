# Validates inputs as characters from the alphabet

def checkstring(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print("\nInput must only contain letters")
            print("There cannot be any numbers (123...), special characters (!@#$...) or whitespaces ( )")
        else:
            return response.title()

question = "Enter your name > "

name = checkstring(question)
print(name)