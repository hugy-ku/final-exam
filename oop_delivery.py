class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return self.name

    def introduce(self):
        print(f"Hi, I'm {self.__name}.")


class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.__address = address
        self.__orders = []

    @property
    def orders(self):
        return self.__orders    
    @property
    def address(self):
        return self.__address

    def place_order(self, item):
        order = DeliveryOrder(self, item)
        self.__orders.append(order)
        return order
    
    def remove_order(self, order):
        try:
            self.__orders.remove(order)
            return True
        except ValueError:
            print("Order not found.")
            return False


class DeliveryOrder:
    def __init__(self, customer: Customer, item):
        self.__customer = customer
        self.__item = item
        self.__status = "preparing"
        self.__driver = "None"

    @property
    def item(self):
        return self.__item
    @property
    def customer(self):
        return self.__customer
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
        driver.add_order(self)
    
    def summary(self):
        print("Order Summary:")
        print(f"Item: {self.__item}")
        print(f"Customer: {self.__customer}")
        print(f"Status: {self.__status}")
        print(f"Driver: {self.__driver}")


class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.__vehicle = vehicle
        self.__orders = []
    
    @property
    def vehicle(self):
        return self.__vehicle
    @property
    def orders(self):
        return self.__orders
    
    def add_order(self, order):
        self.__orders.append(order)

    def remove_order(self, order):
        try:
            self.__orders.remove(order)
            return True
        except ValueError:
            print("Order not found.")
            return False

    def deliver(self, order: DeliveryOrder):
        if order.driver != self:
            print("The order is assigned to another driver.")
            return
        if not order.customer.remove_order(order) or not self.remove_order(order):
            return

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
