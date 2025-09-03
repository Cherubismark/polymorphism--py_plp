# Base Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price   # encapsulated (private attribute)

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... ")

    def get_price(self):
        return f"The price of {self.brand} {self.model} is ${self.__price}"

# Inherited Class
class SmartPhoneWithCamera(Smartphone):
    def __init__(self, brand, model, price, camera_megapixels):
        super().__init__(brand, model, price)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"{self.brand} {self.model} takes a {self.camera_megapixels}MP photo! ")

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", 900)
phone1.call("0722334455")
print(phone1.get_price())

phone2 = SmartPhoneWithCamera("Apple", "iPhone 15", 1200, 48)
phone2.take_photo()
phone2.call("0112233445")
