# Product class
class Product(object):

    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        self.displayInfo()
    
    def displayInfo(self):
        print   "Price : ", str(round(self.price,2))
        print   "Item name: ", self.item_name
        print   "Weight: ", str(self.weight)
        print   "Brand: ", self.brand
        print   "Cost: ", str(self.cost)
        print   "Status: ", self.status
        print   "______________________________" 

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.price *= (1+tax)
        return price 

    def return_product(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "opened":
            self.status = "used"
            self.price = self.price * 0.80
        else:
            self.status = "for sale"
        return self

# Instance1 = product || defective
prod = Product(38.81, "KCM1202OB 12-Cup", 6.2, "KitchenAid", 18.34) 
prod.return_product("defective")
prod.displayInfo()

# # Instance2 = product || in box
prod = Product(34.99, "Beach 46205 12-Cup", 5.29 , "Hamilton", 12.97) 
prod.return_product("in box")
prod.displayInfo()

# # # Instance3 = product || opened
prod = Product(79.99, "KCM1204OB 12-Cup ", 7, "KitchenAid ", 32.87) 
prod.return_product("opened")
prod.displayInfo()
