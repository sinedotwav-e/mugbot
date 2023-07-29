# Final copy (changes can be made later)
# Allows user to order for either delivery or click-and-collect
import time

def valint():
    while True:
        try:
            num = int(input(""))
            if num >= 1 and num <= 2:
                return num
            else:
                print("Input must be either 1 or 2")
        except ValueError:
            print("Invalid input. Input must be 1 or 2")
    
print("Enter a number between 1 or 2")

answer = valint()

print(answer)