
# Declare a class Bike

class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print ("Bike's prince:  $" + str(self.price)) 
        print ("Maximum speed: " + str(self.max_speed))
        print ("Total miles: " + str(self.miles))

    def ride(self):
        print "Riding"
        print self.max_speed
        self.miles += 10

    def reverse(self):
        print "Reversing"
        print self.max_speed
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0

# First instance
ride1 = Bike(200.00, 25)
ride1.ride()
ride1.ride()
ride1.ride()
ride1.reverse()
ride1.displayInfo()

# Second instance
ride2 = Bike(234.34, 45)
ride2.ride()
ride2.ride()
ride2.reverse()
ride2.reverse()
ride2.displayInfo()

# third instance
ride3 = Bike(7045.34, 75)
ride3.reverse()
ride3.reverse()
ride3.reverse()
ride3.displayInfo()
