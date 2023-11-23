class Rectangle:
    def __init__(self, l=1, b=1):
        self.length = l
        self.breadth = b
    
    def perimeter(self):
        return 2*(self.length + self.breadth)
    
    def area(self):
        return self.length * self.breadth

    # Static method : it does not uses the any members of the class
    @staticmethod 
    def isSquare(l, b):
        return l == b

r1 = Rectangle(2, 3)
print(Rectangle.isSquare(10, 10))