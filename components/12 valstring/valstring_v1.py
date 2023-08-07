# Validates inputs as characters from the alphabet

question = "Enter your name > "

while True:
    response = input(question)
    x = response.isalpha()
    if x == False:
        print("\nInput must only contain letters")
        print("There cannot be any numbers (123...), special characters (!@#$...) or whitespaces ( )")
    else:
        print(response.title())
        break

