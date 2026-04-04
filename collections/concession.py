menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = {}  # Dictionary to store items and their quantities
total = 0

# Display Menu
print("------------------MENU--------------------")
for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
print("-------------------------------------------")

# Taking Orders
while True:
    food = input("Select an item (q to quit): ").lower()
    
    if food == "q":
        break
    elif food in menu:
        quantity = input(f"Enter quantity for {food}: ")
        
        if quantity.isdigit():
            quantity = int(quantity)
            if quantity > 0:
                cart[food] = cart.get(food, 0) + quantity  # Update quantity
            else:
                print("Quantity should be greater than 0.")
        else:
            print("Invalid quantity. Please enter a number.")
    else:
        print("Item not on the menu. Please try again.")

# Calculating Total and Displaying Cart
print("\n----------- Your Order -----------")
for food, quantity in cart.items():
    cost = menu[food] * quantity
    total += cost
    print(f"{food} x{quantity} - ${cost:.2f}")

print("---------------------------------")
print(f"Total: ${total:.2f}")
