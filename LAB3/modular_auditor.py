inventory = 0
failedentry = 0
delivery = 0
totaltax = 0.0

while True:
    stock = input ("Enter stock quantity (Type 'Quit' to exit): ")
    if stock.lower() == "quit":
        break

    if not stock.isdigit():
        print ("Error: Enter a valid number.")
        failedentry += 1
        continue

    inventory += int(stock)
    tax = int(stock) * 0.10
    totaltax = tax + totaltax
    delivery += 1


print("\nTotal Unit:", inventory)
print("Number of Failed/Rejected Entries:", failedentry)
print ("Total Tax:", f"{totaltax:.2f}")
print("Number of Successful Deliveries:", delivery)