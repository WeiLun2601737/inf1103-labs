import json
from pathlib import Path

INVENTORY_FILE = Path(__file__).resolve().parent / "inventory.json"

class Product:
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    def update_stock(self, quantity):
        self._stock = quantity

    def display_information(self):
        print(
            f'ID: {self._product_id} | '
            f'Name: {self._name} | '
            f'Price: ${self._price:.2f} | '
            f'Stock: {self._stock}'
        )

    def to_dictionary(self):  # Convert the Product object to a dictionary for JSON saving.
        return {
            "ID": self._product_id,
            "Name": self._name,
            "Price": self._price,
            "Stock": self._stock
        }

    @classmethod
    def from_dictionary(cls, data):  # Create a Product object from a dictionary read from JSON.
        return cls(
            data["ID"],
            data["Name"],
            data["Price"],
            data["Stock"]
        )


class Inventory:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def search_product(self, product_id):
        for product in self._products:
            if product.to_dictionary()["ID"] == product_id:
                return product
        return None

    def display_all(self):
        if len(self._products) == 0:
            print("Inventory is empty.")
            return

        print("\nCurrent Inventory")
        print("-" * 70)

        for product in self._products:
            product.display_information()

        print("-" * 70)

    def product_id_count(self):
        count = len(self._products) + 1
        return f"P{count:03d}"

    def to_list(self):
        return [product.to_dictionary() for product in self._products]


def heading():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")


def menu():
    print("----------- MENU -----------")
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

    product = Product(product_id, name, price, stock)
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
            json.dump(inventory.to_list(), file, indent=1)

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