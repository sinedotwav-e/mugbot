import os
import time

clr = os.system('cls' if os.name == 'nt' else "printf '\033c'")

clr
print("Hello!")
time.sleep(3)
clr
print("Goodbye!!!")
