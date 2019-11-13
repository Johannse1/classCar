from classCar import Car


make = input("Make: ")
model = input("Model: ")
mileage = input("Mileage: ")
price = input("Price: ")
color = input("Color: ")

car = Car(make,model,mileage,price,color)

car.description()
