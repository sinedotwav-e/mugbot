# To allow the user to confirm their order

print("Please confirm your order")
print("Enter 1 to confirm your order")
print("Enter 2 to cancel your order")

while True:
    try:
        confirm = int(input("Enter a number > "))
        if confirm == 1:
            print("Ordered confirmed!")
            break
        elif confirm == 2:
            print("Re-doing order...")
            break
        else:
            print("Invalid number! Enter either 1 or 2")

    except ValueError:
        print("Invalid entry! Enter either 1 or 2")