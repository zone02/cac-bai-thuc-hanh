class Circle(object):
    def __init__(self, r):
        self.radius = r
############################
    def area(self):
        return self.radius**2*.14

aCircle=Circle(2)
print (aCircle.area())


b=Circle(100)
print (b.area())
