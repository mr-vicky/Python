class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    
    def getLength(self):
        return self.length

    def getBreadth(self):
        return self.breadth
    
    def setLength(self, l):
        self.length = l
    
    def setBreadth(self, b):
        self.breadth = b

if __name__=="__main__":
    r1 = Rectangle(4, 2)
    print(r1.getLength())
    print(r1.getBreadth())

    r1.setLength(6)
    r1.setBreadth(3)
    print(r1.getLength(), r1.getBreadth())