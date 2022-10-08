def isPrimenumber(number):
    t = 0
    for i in range (2,number):
        if number%2 == 0:
            t = t+1
            
    if t > 0:
        print("This is not prime number")
    else:
        print("This is prime number")

isPrimenumber(678232)
            