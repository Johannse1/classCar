# Evan Johanns
# class Car
# 11/11/19


class Car():
# comments don't seem to be necessary at the moment as there isn't much code yet
    def __init__(self,make,model,mileage,price,color):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = price
        self.color = color

    def description(self):
            print(f"The car is made by {self.make} ")
            print(f"The model is a {self.model}")
            print(f"The Mileage of the car is {self.mileage}")
            print(f"The price of the car is {self.price}")
            print(f"The color of the car is {self.color}")





