from classes import Supplier, PhysicalProduct, DigitalProduct, Inventory, Order, show_product_details

supplier = Supplier("S001", "ABABABAB Electronics", "ABABABA@gmail.com")

laptop = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5, supplier)
software = DigitalProduct("P002", "Software", 50, 10, 500, supplier)

print("=== Association ===")
del supplier
laptop.supplier.display_information()

print("\n=== Aggregation ===")
inventory = Inventory()
inventory.add_product(laptop)
inventory.remove_product("P001")
laptop.display_information()

print("\n=== Composition ===")
order1 = Order("P001")
order2 = Order("P002")

order1.add_order_line(laptop, 2)
order2.add_order_line(laptop, 1)

print("Different OrderLines:", order1.order_lines[0] is not order2.order_lines[0])
print("Same Product:", order1.order_lines[0].product is order2.order_lines[0].product)

print("\n=== LSP ===")
show_product_details(laptop)
show_product_details(software)

print("\n=== Polymorphism ===")
inventory.add_product(laptop)
inventory.add_product(software)
inventory.display_fulfilment_details()