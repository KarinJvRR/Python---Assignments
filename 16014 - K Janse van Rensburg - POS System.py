#a class is for creating objects. Classes define a set of attributes and methods that the created objects can have.This is the class for items. It defines that tiems will have a name, price, quantity and and currency.
class Item:
    def __init__(self, name, price, quantity, currency='R'):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.currency = currency

#Below is the class for the POS sytem. With all the functions defined that can be done by the POS. 
class POS:
# __init__ is a special method called the constructor. It is automatically called when an object of a class is created. The purpose of __init__ is to initialize the object's attributes and perform any setup required for the object.
    def __init__(self, currency='R'):
        self.inventory = {}
        self.cart = []
        self.currency = currency

#Defines function that will add item to the inventory. 
    def add_to_inventory(self, name, price, quantity):
        if name in self.inventory:
            self.inventory[name].quantity += quantity
        else:
            self.inventory[name] = Item(name, price, quantity, self.currency)

#Defines function that will view what items are in the inventory. 
    def view_inventory(self):
        print("\nInventory:")
        for item_name, item in self.inventory.items():
            print(f"{item_name} - {item.currency}{item.price:.2f} - {item.quantity} in stock")

#Defines function that will add items to the cart. The if will add the items to the cart as long as there is stock on inventory, if there is no stock the else function will print an error. 
    def add_to_cart(self, name, quantity):
        if name in self.inventory and self.inventory[name].quantity >= quantity:
            self.cart.append((name, self.inventory[name].price, quantity, self.currency))
            self.inventory[name].quantity -= quantity
            print(f"Added {quantity} of {name} to cart")
        else:
            print(f"Item {name} is not available or insufficient quantity in inventory")

#Defines function that will show what items have been added to the cart and show the cart total. 
    def view_cart(self):
        print("\nCart:")
        total = 0
        for item in self.cart:
            print(f"{item[0]} - {item[3]}{item[1]:.2f} - {item[2]} pcs")
            total += item[1] * item[2]
        print(f"Total: {self.currency}{total:.2f}")

#Defines function that will checkout the cart and print the receipt. It will also clear the cart after the checkout. 
    def checkout(self):
        print("\nReceipt:")
        total = 0
        for item in self.cart:
            print(f"{item[0]} - {item[3]}{item[1]:.2f} - {item[2]} pcs")
            total += item[1] * item[2]
        print(f"Total: {self.currency}{total:.2f}")
        self.cart = []  # Clear the cart after checkout

#defines a function named main that serves as the entry point of the program. When the POS in entered the Name and 6 options will appear. 
def main():
    pos_system = POS(currency='R')  # Set the currency symbol here

    while True:
        print("\nKarin's Sol-Tech Shop")
        print("1. Add item to inventory")
        print("2. View inventory")
        print("3. Add item to cart")
        print("4. View cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice: ")

#if is a conditional statement that allows you to execute a block of code only if a specified condition is true.
        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            pos_system.add_to_inventory(name, price, quantity)

#elif is a keyword that stands for "else if." It is used in conditional statements to check multiple conditions sequentially. When an if statement's condition is false, the elif statement is evaluated. If the elif condition is true, its corresponding block of code is executed. If none of the conditions are true, the optional else block is executed.
        elif choice == '2':
            pos_system.view_inventory()
        elif choice == '3':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            pos_system.add_to_cart(name, quantity)
        elif choice == '4':
            pos_system.view_cart()
        elif choice == '5':
            pos_system.checkout()
        elif choice == '6':
            print("Exiting the Sol - Tech Shop. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

#this code will take you back to the entry point of the POS. With the name and the 6 options. 
if __name__ == "__main__":
    main()
