class Rectangle:
    count = 0 # class variable or static variable

    def __init__(self, l=1, b=1):
        self.length = l
        self.breadth = b
        Rectangle.count += 1
    
    def perimeter(self):
        return 2*(self.length + self.breadth)
    
    def area(self):
        return self.length * self.breadth
    
    # class method -->
    @classmethod
    def countRectangle(self):
        print(Rectangle.count)
    
if __name__=='__main__':
    r1 = Rectangle(2, 4)
    Rectangle.countRectangle()
    r2 = Rectangle(4, 5)
    Rectangle.countRectangle()
