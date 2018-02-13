# PART I
# Create a Python class called MathDojo that has the methods add and subtract.
# Have these 2 functions take at least 1 parameter.
# Then create a new instance called md. It should be able to do the following task:
#
# md.add(2).add(2,5).subtract(3,2).result
#
# PART II
# Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter
# with any number of values passed into the list. It should now be able to perform
# the following tasks:
#
# md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
#
# PART III
# Make any needed changes in MathDojo in order to support tuples of values in
# addition to lists and singletons.


class MathDojo(object):
    def __init__(self):
        self.sum = 0
    def add(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for value in arg:
                    self.sum += value
            else:
                self.sum += arg
        return self

    def subtract(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for value in arg:
                    self.sum -= value
            else:
                self.sum -= arg
        return self


md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).sum #result = 4
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).sum #result 28.15
