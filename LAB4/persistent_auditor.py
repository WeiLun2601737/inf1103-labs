def get_valid_input():
    itemname = input("Enter item name (Type 'Quit' to exit): ")
    if itemname.lower() == "quit":
            return "quit"

    if itemname.isdigit():
            print ("Error: Enter a valid item name.")
            return None

    if itemname.strip() == "":
            print ("Error: Item name cannot be empty.")
            return None

    stock = input ("Enter stock quantity: ")

    if not stock.isdigit():
            print ("Error: Enter a valid number.")
            return None

    return (itemname, int(stock))

def generate_report(history1,failedentry3, delivery4):
    print("\nNew Order Added:")
    for itemname, stock in history1:
        print(f"Item: {itemname}, Stock: {stock}")
    print("\nNumber of Failed/Rejected Entries:", failedentry3)
    print("Number of Successful Deliveries:", delivery4)
    print("\nOrder successfully saved to inventory.txt")

def save_inventory(history1, filename = "inventory.txt"):
    count = 1
    try:
      with open(filename, "r") as file:
          for line in file: 
                if line.startswith("Order Number"):
                    count += 1
    except FileNotFoundError:
        pass

    with open(filename, "a") as file:
        file.write("Order Number " + str(count) + ":" + str(history1) + "\n")
            
def load_inventory(filename = "inventory.txt"):
     with open(filename, "r") as file:
      data = file.read()
      print(data, end="")

inventory = 0
failedentry = 0
delivery = 0
history = []
    
while True:
    result = get_valid_input()
    if result == "quit":
        break
    if result is None:
        failedentry += 1
        continue

    itemname, stock = result
    history.append((itemname, stock))
    delivery += 1

save_inventory(history)

print("\n================================")
print("Order History:")
print("================================")
load_inventory()
print("================================")
generate_report(history, failedentry, delivery)





