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

def generate_report(total_units,failed_attempts):
    print("\nTotal Units:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

inventory = 0
failedentry = 0
delivery = 0
totaltax = 0
    
while True:
    stock = get_valid_input()
    if stock == "quit":
          break
    if stock is None:
        failedentry += 1
        continue

    inventory = process_delivery(inventory, int(stock))
    totaltax += calculate_tax(int(stock))
    delivery += 1

generate_report(inventory, failedentry)
print ("Total Tax: $", f"{totaltax:.2f}")
print("Number of Successful Deliveries:", delivery)