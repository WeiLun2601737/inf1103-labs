inventory = 0
failedentry = 0

while True:
    stock = input("Enter stock item (or 'quit to finish): ")
    if stock.lower() == "quit":
        break

    if not stock.isdigit():
        print("Error: Please enter a valid number.")
        failedentry += 1
        continue

    if int(stock) < 0:
        print("Error: Number cannot be negative.")
        fentry += 1
        continue


    stock = int(stock)
    inventory += stock

    if int(inventory)>500:
            print("Error: Overstock!")

print("\nTotal Unit:", inventory)
print("Number of Failed/Rejected Entries:", failedentry)
