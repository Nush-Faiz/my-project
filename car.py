from fuel import Fuel

class Car:
    def __init__(self,brand,model, speed=0, fuel_type="Petrol"):
        self.name = brand
        self.model = model
        self.speed = speed
        self.fuel = Fuel(fuel_type)

    def display_info(self):
        print(f"Car brand: {self.name}, Model: {self.model}, speed: {self.speed}km/h, Fuel: {self.fuel.fuel_type}")
