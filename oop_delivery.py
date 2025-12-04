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
        return DeliveryOrder(self, item)


class DeliveryOrder:
    def __init__(self, customer: Customer, item):
        self.customer = customer
        self.item = item
        self.status = "preparing"
        self.driver = "None"

    def assign_driver(self, driver):
        self.driver = driver
    
    def summary(self):
        result = []
        result.append("Order Summary:")
        result.append(f"Item: {self.item}")
        result.append(f"Status: {self.status}")
        result.append(f"Driver: {self.driver}")


class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle
    
    def deliver(self, order: DeliveryOrder):
        print(f"{self.name} is delivering {order.item} to {order.customer.name} using {self.vehicle}.")
        order.status = "delivered"
