# Exit sequence 
import time

exittitle = [
    '░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗██╗',
    '██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝██║',
    '██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░██║',
    '██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░╚═╝',
    '╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗██╗',
    '░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝',
    ]

# Gets the number of items in a list
exitlength = len(exittitle)

# for loop that prints each item in the list one after the other with a delay for each item in the list
for count in range (exitlength):
    print(exittitle[count])
    time.sleep(0.125)

print("Exiting in 3...")
time.sleep(1)
print("Exiting in 2...")
time.sleep(1)
print("Exiting in 1...")
time.sleep(1)