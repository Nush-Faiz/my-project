class Car:
    name = ""
    def __init__(self,brand,model):
        self.name = brand
        self.model = model

    def display_info(self):
        print(f"Car brand: {self.name}, Model:{self.model}")
