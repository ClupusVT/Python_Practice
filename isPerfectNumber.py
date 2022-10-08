def isPerfectnumber(number):
    t = 0
    for i in range (1,number):
        if number%i == 0:
            t = t + i
            #print(t)
            
    if t == number:
        print ("This is perfect number")
    else:
        print ("This is not perfect number")

while True:        
    number = int(input("Enter checked number:"))
    isPerfectnumber(number)
    process = input("Your next action:")
    if process == "exit":
        break
   
