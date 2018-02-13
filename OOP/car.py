class Car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = "15%"
        else:
            self.tax = "12%"

    def display_all(self):
        print "Price = {}" .format(self.price)
        print "Speed = {}" .format(self.speed)
        print "Fuel_Level = {}" .format(self.fuel)
        print "Mileage = {}" .format(self.mileage)
        print "Tax = {}" .format(self.tax)

sports_car = Car(55000, "110mph", "full", "8mpg")
luxury_car = Car(45000, "90mph", "half full", "14mpg")
compact_car = Car(20000, "85mph", "quarter full", "35mph")

sports_car.display_all()
print "-"* 70
luxury_car.display_all()
print "-"* 70
compact_car.display_all()
