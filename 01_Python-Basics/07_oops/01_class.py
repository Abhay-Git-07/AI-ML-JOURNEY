# Create a car class with attributes like brand and model.Then create an instance of this class.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)


my_car_2 = Car("Tata", "Safari")
print(my_car_2.brand)
print(my_car_2.model)

