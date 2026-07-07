# Add a class variable to car that keeps the track of no of cars created

class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1     

    def full_name(self):
        return f"{self.brand} {self.model}" 
    
    def fuel_type(self):
        return "Petrol or Diesel"

class Electric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size 

    def fuel_type(self):
        return "Electric Charge"
    
my_car = Car("Tata", "Safari")
print(my_car.fuel_type())

my_ElectricCar = Electric_Car("Tesla", "S", "85kWh")
print(my_ElectricCar.fuel_type())

my_ElectricCar = Electric_Car("Jaguar", "M", "70kWh")
print(my_ElectricCar.full_name())

print(Car.total_car)  # Ye print kr dega kitni baar Car fn ko call ki gyi ya kitni car bni
