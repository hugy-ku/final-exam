class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Hi, I'm {self.name}.")


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
        print("Order Summary:")
        print(f"Item: {self.item}")
        print(f"Status: {self.status}")
        print(f"Driver: {self.driver.name}")


class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle
    
    def deliver(self, order: DeliveryOrder):
        print(f"{self.name} is delivering {order.item} to {order.customer.name} using {self.vehicle}.")
        order.status = "delivered"

if __name__ == "__main__":
    alice = Customer("Alice", "A")
    bob = Customer("Bob", "B")
    david = Driver("David", "motorcycle")

    alice.introduce()
    bob.introduce()
    david.introduce()
    print()

    order1 = alice.place_order("Laptop")
    order2 = bob.place_order("Headphones")

    order1.assign_driver(david)
    order2.assign_driver(david)

    order1.summary()
    print()
    order2.summary()
    print()
