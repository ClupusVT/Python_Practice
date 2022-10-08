a = int(input())
b = int(input())

def power(a, b):
    t = 0
    h = 1
    for t in range (b):
        h = h*a
        
    print (h)
    
power(a,b)