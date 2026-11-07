from abc import ABC, abstractmethod

class Supplier():

    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email

    def display_information(self) -> None:
        print(f'ID: {self.supplier_id} | Name: {self.name} | Email: {self.contact_email}')

class Product(ABC):
    def __init__ (self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.supplier = supplier

    def update_stock(self, quantity: int) -> None:
        self.__stock = quantity

    def display_information(self, end: str = "\n") -> None:
        print(
            f'ID: {self.__product_id} | '
            f'Name: {self.__name} | '
            f'Price: ${self.__price:.2f} | '
            f'Stock: {self.__stock}',
            end=end
         )

    def to_dictionary(self) -> dict:  # Convert the Product object to a dictionary for JSON saving.
        return {
            "ID": self.__product_id,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock,
            "Supplier": {
                "ID": self.supplier.supplier_id,
                "Name": self.supplier.name,
                "Email": self.supplier.contact_email
            }
        }

    @classmethod
    def from_dictionary(cls, info: dict) -> "Product":  # Takes Data from Json and converts it into a Python Object
        
        supplier_info = info.get("Supplier")

        supplier = Supplier(
            supplier_info["ID"],
            supplier_info["Name"],
            supplier_info["Email"]
        )
        
        if info["Type"] == "Physical":
            return PhysicalProduct(
                info["ID"],
                info["Name"],
                info["Price"],
                info["Stock"],
                info["Weight"],
                supplier
            )
        elif info["Type"] == "Digital":
            return DigitalProduct(
                info["ID"],
                info["Name"],
                info["Price"],
                info["Stock"],
                info["Megabytes"],
                supplier
            )
        else:
            raise ValueError("Unknown Product type")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

class Inventory():
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product : Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> None:
        for product in self.__products:
            if product.to_dictionary()["ID"] == product_id:
                self.__products.remove(product)
                return

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.to_dictionary()["ID"] == product_id:
                return product
        return None

    def display_all(self) -> None:
        if len(self.__products) == 0:
            print("Inventory is empty.")
            return

        print("\nCurrent Inventory")
        print("-" * 70) #"line"

        for product in self.__products:
            product.display_information()
            print("Supplier Information:")
            product.supplier.display_information()
            print()

        print("-" * 70) #"line"

    def display_fulfilment_details(self) -> None:
        for product in self.__products:
            product.display_information()
            print(product.get_fulfilment_info())
            print()

    def product_id_count(self) -> str:
        count = len(self.__products) + 1
        return f"P{count:03d}"

    def tojsonfile(self) -> list[dict]:
        return [product.to_dictionary() for product in self.__products]

class OrderLine():

    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.product._Product__price * self.quantity

class Order():

    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0

        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()

        return total
    
class CanBeShipped(ABC):
    @abstractmethod
    def calculated_shipping_cost(self) -> float:
        pass

class PhysicalProduct(Product, CanBeShipped):

    def __init__ (self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight

    def display_information(self) -> None:
        super().display_information(end = "")
        print(
            f' | Weight: {self.__weight}KG'
            f' | Shipping Cost: ${self.calculated_shipping_cost():.2f}'
        )

    def get_fulfilment_info(self) -> str:
        return f'The {self._Product__name} is physical shipping'

    def calculated_shipping_cost(self) -> float:
        return self.__weight * 5

    def to_dictionary(self) -> dict:
        info = super().to_dictionary()
        info["Type"] = "Physical"
        info["Weight"] = self.__weight
        return info

class DigitalProduct(Product):

    def __init__ (self, product_id: str, name: str, price: float, stock: int, megabytes: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__megabytes = megabytes

    def display_information(self) -> None:
        super().display_information(end = "")
        print(f' | Download Size: {self.__megabytes}MB')

    def get_fulfilment_info(self) -> str:
        return f'This {self._Product__name} is delivered digitally.'

    def to_dictionary(self) -> dict:
        info = super().to_dictionary()
        info["Type"] = "Digital"
        info["Megabytes"] = self.__megabytes
        return info

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


