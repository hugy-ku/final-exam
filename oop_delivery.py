class Person:
    def __init__(self, name):
        self.__name = name
    
    def introduce(self):
        print(f"Hi, I'm {self.__name}.")
    
    @property
    def name(self):
        return self.__name
    
    def __str__(self):
        return self.name


class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.__address = address
    
    def place_order(self, item):
        return DeliveryOrder(self, item)
    
    @property
    def address(self):
        return self.__address



class DeliveryOrder:
    def __init__(self, customer: Customer, item):
        self.customer = customer
        self.__item = item
        self.__status = "preparing"
        self.__driver = "None"

    @property
    def item(self):
        return self.__item
    
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, new_status):
        self.__status = new_status
    
    @property
    def driver(self):
        return self.__driver

    def assign_driver(self, driver):
        self.__driver = driver
    
    def summary(self):
        print("Order Summary:")
        print(f"Item: {self.__item}")
        print(f"Status: {self.__status}")
        print(f"Driver: {self.__driver}")


class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.__vehicle = vehicle
    
    @property
    def vehicle(self):
        return self.__vehicle
    
    def deliver(self, order: DeliveryOrder):
        print(f"{self.name} is delivering {order.item} to {order.customer} using {self.vehicle}.")
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

    david.deliver(order1)
    david.deliver(order2)
    print()

    print("Final Status:")
    print(f"Order for {order1.item} → {order1.status}")
    print(f"Order for {order2.item} → {order2.status}")