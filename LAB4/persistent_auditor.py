def get_valid_input():
    stock = input ("Enter stock quantity (Type 'Quit' to exit): ")

    if stock.lower() == "quit":
            return "quit"
    
    if not stock.isdigit():
            print ("Error: Enter a valid number.")
            return None

    return int(stock)

def process_delivery(current_total,new_value):
      current_total += new_value
      return current_total

def calculate_tax(stock):
    tax = stock * 0.10
    return tax

def generate_report(history1,inventory2,failedentry3, delivery4,totaltax5):
    print("\nNew Stock Added:")
    print(history1)
    print("Total Stock:", inventory2)
    print("Number of Failed/Rejected Entries:", failedentry3)
    print("Number of Successful Deliveries:", delivery4)
    print("Total Tax: $", f"{totaltax:.2f}")
#def load_inventory():
    
            
#def save_inventory():

inventory = 0
count = 1
failedentry = 0
delivery = 0
totaltax = 0
history = []
    
while True:
    stock = get_valid_input()
    if stock == "quit":
          break
    if stock is None:
        failedentry += 1
        continue

    history.append(int(stock))

    inventory = process_delivery(inventory, int(stock))
    totaltax += calculate_tax(int(stock))
    delivery += 1


with open("inventory.txt", "r") as file:
      for line in file: 
            if line.startswith("Stock History "):
                count += 1
      
with open("inventory.txt", "a") as file:
    
        file.write("Stock History " + str(count) + ":" + str(history) + "\n")
print("\n================================")
print("Order History:")
print("================================")
with open("inventory.txt", "r") as file:
      data = file.read()
print(data, end="")
print("================================")
generate_report(history, inventory, failedentry, delivery, totaltax)





