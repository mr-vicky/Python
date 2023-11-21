class Cuboid:
    def __init__(self, l=1, b=1, h=1):
        self.length = l
        self.breadth = b
        self.height = h

    def lidArea(self):
        return self.length * self.breadth
    
    def totalArea(self):
        return 2*(self.length * self.breadth * self.height)
    
    def volume(self):
        return self.length * self.breadth * self.height
    
c1 = Cuboid(10, 20, 30)
print(c1.lidArea())
print(c1.totalArea())
print(c1.volume())
print("\n")

c2 = Cuboid(2, 3, 4)
print(c2.lidArea())
print(c2.totalArea())
print(c2.volume())
print("\n")

# Constructors cannot be overloaded in python, but in python constructors can be called in different ways using the concept of default arguments ->
c3 = Cuboid()
print(c3.volume())

c4 = Cuboid(3)
print(c4.volume())

c5 = Cuboid(3, 4)
print(c5.volume())

c6 = Cuboid(3, 4, 5)
print(c6.volume())