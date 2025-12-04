class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Hi, I'm {self.name}")

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
    
    def place_order(self, item):
        # return DeliveryOrder
        pass

class DeliveryOrder:
    pass