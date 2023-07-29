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

for xt in range (3, 0, -1):
    print(f"Exiting in {xt}...")
    time.sleep(1)
exit()