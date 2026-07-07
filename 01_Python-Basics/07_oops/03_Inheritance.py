# Create an Electric car class that inherits from Car class and has an additional attribute battery_size

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}" 

class Electric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size  

my_tesla = Electric_Car("Tesla", "Model S", "85kWh")

print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)       
print(my_tesla.full_name())  

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())
