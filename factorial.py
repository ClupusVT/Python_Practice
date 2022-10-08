
def factorial(x):
    
    if x == 0:
        t = 1
    else:
        t = 1
        for a in range(1,x+1):
            t = t*a
           

    result = "The factorial of {0} is {1}"
    print(result.format(x,t))
    return t

factorial(10)