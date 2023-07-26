# Title banner, should look appealing to the user
import time

time.sleep(1)

def title():
    title = [
    '███╗   ███╗██╗   ██╗ ██████╗ ███████╗██╗  ██╗ ██████╗ ████████╗██╗',
    '████╗ ████║██║   ██║██╔════╝ ██╔════╝██║  ██║██╔═══██╗╚══██╔══╝██║',
    '██╔████╔██║██║   ██║██║  ███╗███████╗███████║██║   ██║   ██║   ██║',
    '██║╚██╔╝██║██║   ██║██║   ██║╚════██║██╔══██║██║   ██║   ██║   ╚═╝',
    '██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║██║  ██║╚██████╔╝   ██║   ██╗',
    '╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝',
    '',
    '                      By Eardwulf Ulan :p                         '
    ]

    # Gets the number of items in a list
    titlelength = len(title)

    # for loop that prints each item in the list one after the other with a delay for each item in the list
    for count in range (titlelength):
        print(title[count])
        time.sleep(0.125)