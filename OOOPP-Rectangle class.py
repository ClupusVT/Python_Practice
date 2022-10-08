class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        #print (self.length)
        t = self.length * self.width
        #print ("Area is:",t)
        return t
        #return self.length * self.width
        
    
    def perimeter(self):
        #print (self.length)
        t = (self.length + self.width) *2
        #print("perimeter:", t)
        #return self.length * self.width 
        return t
    
    def display(self):        
        print ("Area is:",self.area())
        print ("perimeter is:",self.perimeter())
       
     

class Parallelepipede (Rectangle):
    def Volume(self,height):
        c = super().area()
        t1 = c*height
        print ("Volume is:",t1)
        



area1 = Parallelepipede(5,6)
#area1.area()
area1.display()
area1.Volume(7)
