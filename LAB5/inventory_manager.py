import json
def heading():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

def menu():

    print("----------- MENU -----------")
    print("1. Display All Product")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

def add_product(new_products):

    count = len(new_products) + 1
    product_id = "P" + str(count).zfill(3)
    print("Add New Product")
    print("Product ID: ", product_id)

    while True:
        product_name = input("Product Name: ").strip()
        if product_name == "":
          print("Error: Product name cannot be empty.")
        elif product_name.isdigit():
            print("Error: Product name cannot be a number.")
        else:
             break

    while True:
        try:
            product_price = float(input("Price: $").strip())
            if product_price < 0:
                print("Error: Price must be a positive number.")
            else:
                break
        except ValueError:
            print("Error: Price must be a number.")

    while True:
        try:
            product_stock = int(input("Stock Quantity: "))
            if product_stock < 0:
                print("Error: Stock quantity must be a positive number.")
            else:
                break
        except ValueError:
            print("Error: Stock quantity must be a number.")

    print("Product added successfully!")
    
    Newproduct = {
        "ID": product_id,
        "Name": product_name,
        "Price": product_price,
        "Stock": product_stock
    }
    new_products.append(Newproduct)

def update_stock(new_products):
    while True:
        product_id = input("Enter Product ID: ").strip().upper()    
        for data in new_products:
            if product_id == data["ID"]:
                print("Product Found:")
                print("Name: ", data["Name"])
                print("Current Stock: ", data["Stock"])

                while True:
                    try:
                        new_stock = int(input("\nNew Stock Quantity: "))
                        if new_stock < 0:
                            print("Error: Stock quantity must be a positive number.")
                        else:
                            data["Stock"] = new_stock
                            print("\nStock updated successfully!")
                            return
                    except ValueError:
                            print("Error: Stock quantity must be a number.")
        print("Product ID not found. Please try again.")
                        
def search_product(new_products):
    while True:
        print("Search Product")
        product_id = input("Enter Product ID: ").strip().upper()
        for data in new_products:
            if product_id == data["ID"]:
                print("\nProduct Found")
                print("------------------------------------------------")
                print("ID: ", data["ID"])
                print("Name: ", data["Name"])
                print("Price: ", data["Price"])
                print("Stock: ", data["Stock"])
                print("------------------------------------------------")
                return
            
        print("\nProduct ID not found. Please try again.\n")

def display_all(new_products):
        if len(new_products) == 0:
            print("Inventory is empty")
            return
        for value in new_products:
            print(
                 f'ID: {value["ID"]} | '
                 f'Name: {value["Name"]} | '
                 f'Price: ${value["Price"]:.2f} | '
                 f'Stock: {value["Stock"]}'
                )

def load_inventory(filename = "inventory.json"):
    try:
        with open (filename,"r") as file:
            data = json.load(file)
        print("\nInventory.json found.")
        print("Inventory loaded successfully.\n")
        return data
    except FileNotFoundError:
        print("Inventory not Found.")
        return []
    except json.JSONDecodeError:
        print("Inventory is Empty")
        return []
 
def save_inventory(new_products, filename = "inventory.json"):

    try:
        with open(filename, "w") as file:
            json.dump(new_products, file, indent = 1)
        print("Inventory saved to inventory.json.")
    except:
        print("Failed to save inventory to inventory.json")

heading()
new_products = load_inventory()
menu()

while True:
    option = input("\nEnter Option: ").strip()

    if option == "1":
        display_all(new_products)
    elif option == "2":
        add_product(new_products)
    elif option == "3":
        update_stock(new_products)
    elif option == "4":
        search_product(new_products)
    elif option == "5":
        print("Saving Inventory...")
        save_inventory(new_products)
    elif option == "6":
        save_inventory(new_products)
        print("Saving inventory before exit...")
        print("Inventory saved successfully.")
        print("\nThank you for using Inventory Management System.")
        print("Program Terminated.")
        break
    else:
        print("Invalid option. Please key [1-6]")
