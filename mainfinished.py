#Pizza bot program
#24/05/23
#Bugs - phone number allows letters
#     - Name input allow numbers

import sys
import random
from random import randint

#List of random names
names=["Mark", "Pheobe", "Sally", "Michael", "Denise","Ellen", "Eric", "Moana", "Lewis","Lara"]
#Lists of pizza names
pizzanames = ['Margherita','Pepperoni','Hawaiian','Cheese','Italian','Veggie', 'Vegan','Chicken Deluxe', 
               'Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe']
#Lists of pizza prices
pizzaprices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50,13.50, 13.50]

#List to store ordered pizzas
orderlist = []
#List to store pizzas prices
ordercost = []

#Customer details dictionary
customerdetails = {}

#Validates inputs to check they are blank

def notblank(question):
   valid = False
   while not valid:
       response = input(question)
       if response != "":
            return response.title()
       else:
           print("This cannot be blank") 


#Welcome message with random name
def welcome():
    '''
    Purpose: to genrate a random name from the list and print out
    a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("***Welcome to Dream Pizza***")
    print("**My name is",name, "***")
    print("***I will be here to help you order your delicious Dream Pizza*** ")
    
#Menu for pickup or delivery
def ordertype():
    delpick = ""
    print ("Is your order for pickup or delivery")
    print (" For pickup please enter 1 ")
    print (" For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Pickup")
                    delpick = "pickup"
                    pickupinfo()
                    break            
                elif delivery == 2:
                    print ("Delivery")
                    deliveryinfo()
                    delpick = "delivery"
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print ("That is no a valid number")
            print("Please enter 1 or 2")
    return delpick        


#Pick up information- name and phone number
def pickupinfo():
    question = ("Please enter your name ")
    customerdetails['name'] = notblank(question)
    print (customerdetails['name'])

    question = ("Please enter your phone number ")
    customerdetails['phone'] = notblank(question)
    print (customerdetails['phone'])
    print(customerdetails)


#Delivery information - name and address
def deliveryinfo():
    question = ("Please enter your name ")
    customerdetails['name'] = notblank(question)
    print (customerdetails['name'])

    question = ("Please enter your phone number ")
    customerdetails['phone'] = notblank(question)
    print (customerdetails['phone'])
  
    
    question = ("Please enter your house number ")
    customerdetails['house'] = notblank(question)
    print (customerdetails['house'])

    question = ("Please enter your street name ")
    customerdetails['street'] = notblank(question)
    print (customerdetails['street'])

    question = ("Please enter your suburb ")
    customerdetails['suburb'] = notblank(question)
    print (customerdetails['suburb'])

# Pizza menu
def menu():
    numberpizzas = 12

    for count in range (numberpizzas):
        print("{} {} ${:.2f}"  .format(count+1,pizzanames[count],pizzaprices[count]))

list()

#Choose total number of pizzas - max 5
#Pizza order - from menu -print each pizza ordered with cost
def orderpizza():
    #Ask for total number of pizzas for order
    numpizzas = 0
    while True:
        try:
            numpizzas = int(input("How many pizzas do you want to order? "))
            if numpizzas >= 1 and numpizzas <= 5:
                break
            else:
                print("Your order must be between 1 and 5")
        except ValueError:
            print ("That is no a valid number")
            print("Please enter number between 1 and 5")
    #Chosse pizza from menu
    for item in range(numpizzas):
        while numpizzas > 0:
            while True:
                try:
                    pizzaordered = int(input("Please choose your pizzas by entering the number from the menu "))
                    if pizzaordered >= 1 and pizzaordered <= 12:
                        break
                    else:
                        print("Your pizza order must be between 1 and 12")
                except ValueError:
                    print ("That is not a valid number")
                    print("Please enter a number between 1 and 12")
            pizzaordered = pizzaordered -1
            orderlist.append(pizzanames[pizzaordered])
            ordercost.append(pizzaprices[pizzaordered])
            print("{} ${:.2f}" .format(pizzanames[pizzaordered],pizzaprices[pizzaordered]))
            numpizzas = numpizzas-1


#Print order out - including if order is del or pick up and names and price of each pizza - total cost including any delivery charge
def printorder(delpick):
    print()
    totalcost = sum(ordercost)
    print("Your Details")
    if delpick == "pickup":
        print("Your Order is for Pickup")
        print(f"Customer Name:  {customerdetails['name']} \nCustomer Phone: {customerdetails['phone']} ")
    elif delpick == "delivery":
        print("Your Order is for delivery a $5.00 delivery charge applies")
        totalcost = totalcost + 5
        print(f"Customer Name:  {customerdetails['name']} \nCustomer Phone: {customerdetails['phone']}  \nCustomer Address: {customerdetails['house']} {customerdetails['street']} {customerdetails['suburb']}")
    print()
    print("Your Order Details")
    count = 0
    for item in orderlist:
        print("Ordered: {} Cost ${:.2f}" .format(item, ordercost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${totalcost:.2f}")


#Ability to cancel or proceed with order
def confirmcancel():
    print ("Please Confirm Your Order")
    print ("To confirm please enter 1 ")
    print ("To cancel please enter 2")
    while True:
        try:
            confirm = int(input("Please enter a number "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("Order Confirmed")
                    print ("Your Order has been sent to our kitchen")
                    print ("Your delicious pizza will be with you shortly")
                    newexit()
                    break
            
                elif confirm == 2:
                    print ("Your Order has been Cancelled ")
                    print ("You can restart the order ot exit the BOT")
                    newexit()
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print ("That is no a valid number")
            print("Please enter 1 or 2")




#Option for new order or to exit
def newexit():
    print ("Do you want to start another Order or exit")
    print ("To start another order enter 1 ")
    print ("To exit the BOT enter 2")
    while True:
        try:
            confirm = int(input("Please enter a number "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("New Order")
                    orderlist.clear()
                    ordercost.clear()
                    customerdetails.clear()
                    main()
                    break
            
                elif confirm == 2:
                    print ("Exit")
                    orderlist.clear()
                    ordercost.clear()
                    customerdetails.clear()
                    sys.exit()
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print ("That is no a valid number")
            print("Please enter 1 or 2")






#Main function
def main():
    '''
    Purpose: to run all functions
    a welcome message
    Parameters: None
    Returns:None
    '''
    welcome()
    delpick = ordertype()
    menu()
    orderpizza()
    printorder(delpick)
    confirmcancel()
    
    
   
main()

