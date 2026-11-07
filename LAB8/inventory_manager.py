import json
from pathlib import Path
from classes import Product, Inventory, PhysicalProduct, DigitalProduct, Supplier

INVENTORY_FILE = Path(__file__).resolve().parent / "inventory.json"

def heading():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

def menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

def add_product(inventory):
    product_id = inventory.product_id_count()
    print("\nAdd New Product")
    print("Product ID:", product_id)
    print("1. Physical Product")
    print("2. Digital Product")

    while True:
        option = input("Choose Product Type (1 or 2): ").strip()
        if option == '1' or option == '2':
            break
        else:
            print("Enter 1 or 2")

    while True:
        name = input("Product Name: ").strip()
        if name == "":
            print("Error: Product name cannot be empty.")
        elif name.isdigit():
            print("Error: Product name cannot be a number.")
        else:
            break

    while True:
        try:
            price = float(input("Price: $").strip())
            if price < 0:
                print("Error: Price cannot be negative.")
            else:
                break
        except ValueError:
            print("Error: Price must be a number.")

    while True:
        try:
            stock = int(input("Stock Quantity: ").strip())

            if stock < 0:
                print("Error: Stock cannot be negative.")
            else:
                break
        except ValueError:
            print("Error: Stock quantity must be a whole number.")

    while True:
        if option == '1':
            try:
                weight = float(input("Enter Weight (KG): ").strip())

                if weight <=0:
                    print("Enter a positive number")
                else:
                    break
            except ValueError:
                print("Enter a valid number")

        elif option == '2':
            try:
                megabytes = float(input("Enter download size (MB): ").strip())

                if megabytes <= 0:
                    print("Enter a positive number")
                else: 
                    break
            except ValueError:
                print("Enter a valid number")

    if option == '1':
        product = PhysicalProduct(product_id, name, price, stock, weight)
    elif option == '2':
        product = DigitalProduct(product_id, name, price, stock, megabytes)

    inventory.add_product(product)
    print("Product added successfully!")

def update_stock(inventory):

    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product ID not found.")
        return

    print("Product found:")
    product.display_information()

    while True:
        try:
            new_stock = int(input("New Stock Quantity: ").strip())

            if new_stock < 0:
                print("Error: Stock cannot be negative.")
            else:
                product.update_stock(new_stock)
                print("Stock updated successfully!")
                return
        except ValueError:
            print("Error: Stock quantity must be a whole number.")


def search_product(inventory):
    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
    else:
        print("\nProduct found:")
        product.display_information()


def load_inventory(filename=INVENTORY_FILE):
    inventory = Inventory()

    try:
        with open(filename, "r") as file:
            saved_products = json.load(file)

        for data in saved_products:
            product = Product.from_dictionary(data)
            inventory.add_product(product)

        print("\nInventory.json found.")
        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("\nNo inventory file found. Starting with an empty inventory.")

    except json.JSONDecodeError:
        print("\nInventory file is empty or invalid. Starting with an empty inventory.")

    return inventory


def save_inventory(inventory, filename=INVENTORY_FILE):
    try:
        with open(filename, "w") as file:
            json.dump(inventory.tojsonfile(), file, indent=1)

        print("Inventory saved to inventory.json.")

    except OSError as error:
        print("Could not save the inventory:", error)


heading()
inventory = load_inventory()
menu()

while True:
    option = input("\nEnter Option: ").strip()

    if option == "1":
        inventory.display_all()

    elif option == "2":
        add_product(inventory)

    elif option == "3":
        update_stock(inventory)

    elif option == "4":
        search_product(inventory)

    elif option == "5":
        save_inventory(inventory)

    elif option == "6":
        save_inventory(inventory)
        print("\nThank you for using the Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please key [1-6].")

