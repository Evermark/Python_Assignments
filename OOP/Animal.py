# Methods:
# walk: decreases health by one
# run: health decreases by five
# display health: print to the terminal the animal's health.

class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "{} health {}" .format(self.name, self.health)
        return self

# Extend the Animal class to two child classes, Dog and Dragon.
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health
        print "I am a Dragon"
        return self

C = Animal("Cat")
C.walk().walk().walk().run().run().display_health()

D = Dog("goldie")
D.walk().walk().walk().run().run().pet().display_health()

D.fly().display_health()

Y = Dragon("blaze")
Y.fly().fly().run().display_health()
