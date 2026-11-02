from abc import ABC, abstractmethod

class Product(ABC):
    def __init__ (self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self, end= "\n"):
        print(
            f'ID: {self.__product_id} | '
            f'Name: {self.__name} | '
            f'Price: ${self.__price:.2f} | '
            f'Stock: {self.__stock}',
            end=end
         )

    def to_dictionary(self):  # Convert the Product object to a dictionary for JSON saving.
        return {
            "ID": self.__product_id,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock
        }

    @classmethod
    def from_dictionary(cls, info):  # Takes Data from Json and converts it into a Python Object
        if info["Type"] == "Physical":
            return PhysicalProduct(
                info["ID"],
                info["Name"],
                info["Price"],
                info["Stock"],
                info["Weight"]
            )
        elif info["Type"] == "Digital":
            return DigitalProduct(
                info["ID"],
                info["Name"],
                info["Price"],
                info["Stock"],
                info["Megabytes"]
            )
        else:
            raise ValueError("Unknown Product type")

    @abstractmethod
    def get_fulfilment_info(self):
        pass

class Inventory():
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.to_dictionary()["ID"] == product_id:
                return product
        return None

    def display_all(self):
        if len(self.__products) == 0:
            print("Inventory is empty.")
            return

        print("\nCurrent Inventory")
        print("-" * 70) #"line"

        for product in self.__products:
            product.display_information()

        print("-" * 70) #"line"

    def product_id_count(self):
        count = len(self.__products) + 1
        return f"P{count:03d}"

    def tojsonfile(self):
        return [product.to_dictionary() for product in self.__products]
    
class CanBeShipped(ABC):
    @abstractmethod
    def calculated_shipping_cost(self):
        pass

class PhysicalProduct(Product, CanBeShipped):

    def __init__ (self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information(end = "")
        print(
            f' | Weight: {self.__weight}KG'
            f' | Shipping Cost: ${self.calculated_shipping_cost():.2f}'
        )

    def get_fulfilment_info(self):
        print(f'The {self._Product__name} is physical shipping')

    def calculated_shipping_cost(self):
        return self.__weight * 5

    def to_dictionary(self):
        info = super().to_dictionary()
        info["Type"] = "Physical"
        info["Weight"] = self.__weight
        return info

class DigitalProduct(Product):

    def __init__ (self, product_id, name, price, stock, megabytes):
        super().__init__(product_id, name, price, stock)
        self.__megabytes = megabytes

    def display_information(self):
        super().display_information(end = "")
        print(f' | Download Size: {self.__megabytes}MB')

    def get_fulfilment_info(self):
        print(f'This {self._Product__name} is delivered digitally.')

    def to_dictionary(self):
        info = super().to_dictionary()
        info["Type"] = "Digital"
        info["Megabytes"] = self.__megabytes
        return info
