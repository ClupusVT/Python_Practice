class NumberHolder:

   def __init__(self, number,name ):
       self.number = number
       self.name = name

   def returnNumber(self):
       return self.number
   def Helloname(self):
         print("Hello", self.name)    

var = NumberHolder(7,"Nam")
print(var.returnNumber()) #Prints '7'

print(var.Helloname())

i = 0
while i < 6:
   i += 1
   if i == 3:
      continue
   print(i)