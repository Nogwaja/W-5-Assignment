# Base class
class Gadget:
    def __init__(self, name, brand, price, stock_quantity):
        self.name = name
        self.brand = brand
        self.__price = price  # private attribute
        self.__stock_quantity = stock_quantity  # private attribute

    # Getter for price
    def get_price(self):
        return self.__price

    # Setter for price
    def set_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price

    # Getter for stock
    def get_stock_quantity(self):
        return self.__stock_quantity

    # Setter for stock
    def set_stock_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.__stock_quantity = new_quantity

    def display_info(self):
        print(f"Gadget: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Price: R{self.__price}")
        print(f"Stock: {self.__stock_quantity}")

    def update_stock(self, quantity):
        self.__stock_quantity += quantity
        print(f"Updated stock for {self.name}: {self.__stock_quantity}")

    def apply_discount(self, percentage):
        discount_amount = self.__price * (percentage / 100)
        self.__price -= discount_amount
        print(f"New price after {percentage}% discount: R{self.__price:.2f}")


# Subclass: Smartphone
class Smartphone(Gadget):
    def __init__(self, name, brand, price, stock_quantity, operating_system, number_of_cameras):
        super().__init__(name, brand, price, stock_quantity)
        self.operating_system = operating_system
        self.number_of_cameras = number_of_cameras

    def display_info(self):
        super().display_info()
        print(f"Operating System: {self.operating_system}")
        print(f"Cameras: {self.number_of_cameras}")


# Subclass: Laptop
class Laptop(Gadget):
    def __init__(self, name, brand, price, stock_quantity, ram_size, is_touchscreen):
        super().__init__(name, brand, price, stock_quantity)
        self.ram_size = ram_size
        self.is_touchscreen = is_touchscreen

    def display_info(self):
        super().display_info()
        print(f"RAM: {self.ram_size}GB")
        print(f"Touchscreen: {'Yes' if self.is_touchscreen else 'No'}")


# Function demonstrating polymorphism
def show_gadget_info(gadget):
    gadget.display_info()
    print("-" * 30)


