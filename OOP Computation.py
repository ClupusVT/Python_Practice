class Computation:
    # define constructor with attributes: length and width 
    def __init__(self, number):
        self.number = number
        
       
        
    # Create Perimeter method
    def Factorial(self):
        fact = 1
        if self.number == 0:
            break
        else:
           for t in range(self.number):
              fact = fact * t
        
        return fact
    
    # Create Perimeter method
    def Sum(self):
        sum = 0
        for t in range(self.number):
            sum = sum + t

        return sum    
    
    def display(self):
        print("Factorial is: ", self.Factorial())
        print("Sum is: ", self.Sum())
        #print("The perimeter of rectangle is: ", self.Perimeter())
        #print("The area of rectangle is: ", self.Area())



        
x = Computation(5)
x.display()