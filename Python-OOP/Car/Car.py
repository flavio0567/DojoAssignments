# Class Car

class Car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    
    def display_all(self):
        print"Price : ", str(self.price),  ", Speed: ", str(self.speed), "Fuel: ", self.fuel, "Mileage: ", str(self.mileage), "Tax: ", str(self.tax)


# "This would create 1o. object of Car class" - 0.12
car1 = Car(2000,35,"Full",15)

# "This would create 2o. object of Car class" - 0.12
car2 = Car(2000,5,"Not Full",105)

# "This would create 3o. object of Car class" - 0.12
car3 = Car(2000,15,"Kind of Full",95)

# "This would create 4o. object of Car class" - 0.12
car4 = Car(2000,25,"Full",25)

# "This would create 5o. object of Car class" - 0.12
car5 = Car(2000,45,"Empty",25)

# "This would create 6o. object of Car class" - 0.15
car6 = Car(20000000,35,"Empty",15)
