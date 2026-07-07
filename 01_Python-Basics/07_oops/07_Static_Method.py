# Add a static method to the car class that returns a general description of the car

class Car:
    @staticmethod 
    def general_description():
        return "Cars are means of transport"  
    
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1     

    def full_name(self):
        return f"{self.brand} {self.model}" 
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
print(Car.general_description())
my_car = Car("Tata","Safari")
print(my_car.general_description()) #Not able to do what we wanted search for it 
