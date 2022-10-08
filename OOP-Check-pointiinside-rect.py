from random import randint
import turtle

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def checkpointinrectangle(self,rect):
        if (rect.lower.x < self.x < rect.upper.x) and (rect.lower.y < self.y < rect.upper.y):
            print("This point inside rectangle")
        else:
            print("This point outside rectangle")
        
    

class Rectangle:
    def __init__(self,lower,upper):
        self.lower = lower
        self.upper = upper     
    
    def perimeter(self):
        return ((self.upper.x-self.lower.x)+(self.upper.y-self.lower.y))*2
class Area:
    def __init__(self,width,long):
        self.width = width
        self.long = long 
        
    def calculation (self):
       print (self.width*self.long)
       
class GuiRectangle(Rectangle):
        
        
    
    def drawrectangle(self,canvas):
        ##Go to the co-ordinate
        canvas.penup()##mean to take up the pen 
        canvas.goto(self.lower.x,self.lower.y)
        canvas.pendown()
        ##Moving processing
        myturtle.forward(self.upper.x-self.lower.x)
        myturtle.left(90)
        myturtle.forward(self.upper.y-self.lower.y)
        myturtle.left(90)
        myturtle.forward(self.upper.x-self.lower.x)
        myturtle.left(90)
        myturtle.forward(self.upper.y-self.lower.y)
        myturtle.left(90)          
        
        turtle.done
        
myturtle = turtle.Turtle()
gui_rectanlge1 = GuiRectangle(Point(randint(0, 200), randint(0, 200)), Point(randint(200, 400), randint(200, 400)))
gui_rectanlge1.drawrectangle(canvas=myturtle)
print (gui_rectanlge1.perimeter())
##rectangle1 = Rectangle(Point(3,4),Point(8,9))
rectangle1 = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19))) ## use with random function

print("Rectangle Coordinate:",
      rectangle1.lower.x,",",
      rectangle1.lower.y, "and",
      rectangle1.upper.x, "," ,
      rectangle1.upper.y)

point1 = Point(int(input("X:")),int(input("Y:")))
point1.checkpointinrectangle(rectangle1)
area1 = Area((rectangle1.upper.x- rectangle1.lower.x),(rectangle1.upper.y- rectangle1.lower.y))
area1.calculation()