class Rectangle :
    def __init__(self, length, width ):
        self.length = length
        self.width = width

    def Perimeter(self):
        peri = (self.length + self.width) *2
        print("Perimeter is " + peri)

x = Rectangle(3,4)
x.Perimeter