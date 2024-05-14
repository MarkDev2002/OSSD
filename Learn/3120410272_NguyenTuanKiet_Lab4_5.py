class Manufacturer:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def describe(self):
        print(f"I'm from Manufacturer: {self.name} is located in {self.location}")

class Device:
    def __init__(self, name, price, manufacturer):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer

    def describe(self):
        print(f"I'm from Device :  {self.name} price is {str(self.price)}")
        self.manufacturer.describe()

dev1 = Device("iphone", 1000, Manufacturer("apple", "US"))
dev1.describe()

