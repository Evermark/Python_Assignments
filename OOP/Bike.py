class Bike(object):

    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

# this method display the bike's price, maximum speed,
# and the total miles.
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles

# have it display "Riding" on the screen and increase the total
# miles ridden by 10
    def ride(self):
        self.miles = self.miles + 10
        print "Riding"
        return self

# have it display "Reversing" on the screen and decrease the
# total miles ridden by 5...
    def reverse(self):
        if self.miles < 5:
            print "minimum miles ridden, cannot have negative miles"
            return self
        self.miles = self.miles - 5
        print "Reversing"
        return self

mybike = Bike(300, "40mph")
tom_bike = Bike(350,"30mph")
jessica_bike = Bike(400, "35mph")
# first instance ride three times, reverse once and have it displayInfo()
mybike.ride().ride().ride().reverse().displayInfo()
print "-"* 70
# second instance ride twice, reverse twice and have it displayInfo().
tom_bike.ride().ride().reverse().reverse().displayInfo()
print "-"* 70
# third instance reverse three times and displayInfo().
jessica_bike.reverse().reverse().reverse().displayInfo()
