class Car:
    def __init__(self,brand,model, speed=0):
        self.name = brand
        self.model = model
        self.speed = speed

    def display_info(self):
        print(f"Car brand: {self.name}, Model: {self.model}, speed: {self.speed}km/h")
