# Hannah Spicher
# UWYO COSC 1010
# 11/12/24
# Lab 09
# Lab Section: 11
# Sources, people worked with, help given to: W3 Schools textbook, Our textbook, very nice man who sits next to me in lab, older brother, slides
# I have no idea how to do the spacing for the toppings on the receipt
# Comments
# Here

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.

class Pizza:
    def __init__(user_pizza, size, sauce='red'):
        user_pizza.size = max(size, 10) 
        user_pizza.sauce = sauce
        user_pizza.toppings = ['cheese'] 

    def getSize(user_pizza):
        return user_pizza.size

    def getSauce(user_pizza):
        return user_pizza.sauce

    def addTopping(user_pizza, topping):
        user_pizza.toppings.append(topping)

    def getAmountOfToppings(user_pizza):
        return len(user_pizza.toppings)  



# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.

class Pizzeria:
    def __init__(user_pizza):
        user_pizza.orders = 0
        user_pizza.price_per_topping = 0.30
        user_pizza.price_per_inch = 0.60
        user_pizza.pizzas = []

    def placeOrder(user_pizza):
        user_pizza.orders += 1
        size = int(input("Please enter the size of pizza, as a whole number. The smallest size is 10: "))
        sauce = input("What kind of sauce would you like? Default sauce is red sauce: ")
        sauce = sauce if sauce else 'red'
        toppings = []
        topping = input("Please enter the topping you would like to add, if finished hit enter: ")
        while topping:
            toppings.append(topping)
            topping = input("Please enter the topping you would like to add, if finished hit enter: ")

        pizza = Pizza(size, sauce)
        for topping in toppings:
            pizza.addTopping(topping)
        user_pizza.pizzas.append(pizza)

    def getPrice(user_pizza, pizza_index):
        pizza = user_pizza.pizzas[pizza_index]
        size_price = pizza.getSize() * user_pizza.price_per_inch
        topping_price = pizza.getAmountOfToppings() * user_pizza.price_per_topping
        return size_price + topping_price

    def getReceipt(user_pizza, pizza_index):
        pizza = user_pizza.pizzas[pizza_index]
        print(f"You ordered a {pizza.getSize()}\" pizza with {pizza.getSauce()} sauce and the following toppings:")
        for topping in pizza.toppings:
            print(f"{topping}")
        print(f"You ordered a {pizza.getSize()}\" pizza for {pizza.getSize() * user_pizza.price_per_inch:.2f}")
        print(f"You had {pizza.getAmountOfToppings()} toppings for {pizza.getAmountOfToppings() * user_pizza.price_per_topping:.2f}")
        print(f"Your total price is {user_pizza.getPrice(pizza_index):.2f}")

    def getNumberOfOrders(user_pizza):
        return user_pizza.orders

# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.
# Main program
pizzeria = Pizzeria()
while True:
    order = input("Would you like to place an order? Or enter 'exit' to exit: ")
    if order.lower() == 'exit':
        break
    pizzeria.placeOrder()
    pizzeria.getReceipt(pizzeria.getNumberOfOrders() - 1)

print(f"You ordered {pizzeria.getNumberOfOrders()} pizzas.")

# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""