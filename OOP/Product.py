class product(object):

    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self, decimal):
        self.price += round(decimal * self.price, 2)
        return self
    def item_return(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        if reason == "in box opened":
            self.status = "used"
            self.price = self.price * .8
            return self
        if reason == "in box, like new":
            return self
    def display_all():
        print "Price: {}" .format(self.price)
        print "Item: {}" .format(self.item_name)
        print "Weight: {}" .format(self.weight)
        print "Brand: {}" .format(self.brand)
        print "Status: {}" .format(self.status)
