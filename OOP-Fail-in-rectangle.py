import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def fall_in_rectagle(self, checkpoint1, checkpoint2):
        if checkpoint1[0]< self.x <checkpoint2[0] and checkpoint1[1] < self.y< checkpoint2[1]:
            print("Right")
        else:
            print("Fail")
    def check_distace(self, checkpoint):##function distance that collect self comes from main Point and checkpoint it will be created later
         return (self.x-checkpoint.x)*2+(self.y-checkpoint.y)
class Rectangle:
    def __init__(self,lower,upper):
        self.lower = lower
        self.upper = upper
        print(lower)
        print(upper)
class Budget:
    def __init__(self,time,fund):
        self.time = time
        self.fund = fund    
    


point1 = Point(Budget(4,5),Budget(23,12))
print(point1.y.time)
rec1 = Rectangle(Point(Budget(4,5),Budget(101,102)),Point(Budget(4,5),Budget(106,107)))
print (rec1.upper.y.time)
       

        
         
        
    
point2 = Point(1,1)
point3 = Point(4,4)##In this item point 3 will be configured with 2 values that mark it's location , this help us create suitable from that function could utilize
point2.fall_in_rectagle((0,0), (2,3))
print(point2.check_distace(point3))

                
        