class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    
    def getArea(self):
        return self.length * self.breadth

    def getPerimeter(self):
        return 2*(self.length + self.breadth)
    
class Cuboid(Rectangle):
    def __init__(self, l, b, h):
        self.height = h
        super().__init__(l, b)
    
    def getVolume(self):
        return self.length*self.breadth*self.height
    
r1 = Rectangle(10, 5)
print(r1.getArea())
print(r1.getPerimeter())

c1 = Cuboid (30, 20, 10)
print("Volume of Cuboid :", c1.getVolume())