# Validates the phone number input
question = ("Please enter your phone number > ")

PH_LOW = 7
PH_HIGH = 11

while True:
    try:
        num = int(input(question))
        testnum = num
        count = 0
        while testnum > 0:
            testnum = testnum//10
            count = count + 1
        if count >= PH_LOW and count <= PH_HIGH:
            print(num)
            break
        else:
            print("\nNZ Phone Numbers have between 7 or 11 digits.")
    except ValueError:
        print("\nInvalid Input! NZ Phone Numbers have between 7 or 11 digits.")