class Person:
    def __init__(self,name):
        self.name = name
class Customer(Person):
    def __init__(self,name,address):
        super().__init__(name)
        self.address = address
    def place_order(self,item):
        return DeliveryOrder(self.name,item)
    
class Driver(Person):
    def __init__(self,name,vehicle):
        super().__init__(name)
        self.vehicle = vehicle
    def deliver(self,order):
        order.status = "delivered"
        print(f"{self.name} is delivering {order.item} to {order.customer} using {self.vehicle}")
        
class DeliveryOrder:
    def __init__(self,customer,item,status = "preparing"):
        self.customer = customer
        self.item = item
        self.status = status  
    def assign_driver(self,driver):
        self.driver = driver.name
        return self.driver
    def summary(self):
        return f"Order Summary:\nItem: {self.item}\nCustomer: {self.customer}\nStatus: {self.status}\nDriver: {self.driver}"
    




c1 = Customer("Alice","Bangkok")
c2 = Customer("Bob","Bangkok")

order1 = c1.place_order("Laptop")
order2 = c2.place_order("Headphones")
driver = Driver("David","motorcycle")


print(f"Hi, I'm {c1.name}.")
print(f"Hi, I'm {c2.name}.")
print(f"Hi, I'm {driver.name}.")
print()
order1.assign_driver(driver)
order2.assign_driver(driver)
print(order1.summary())
print()
print(order2.summary())
print()
driver.deliver(order1)
driver.deliver(order2)
print()
print("Final Status")
print(f"Order for {order1.item} → {order1.status}")
print(f"Order for {order2.item} → {order2.status}")