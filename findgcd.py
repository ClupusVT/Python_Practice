a = int(input())
b = int(input())

def gcd(a,b):
    if a > b:
        bigger = a
        smaller = b
    else:
        bigger = b
        smaller = a
    t1 = []
    max = 0
    for t in range(1,bigger):
        if bigger % t == 0:
            t1.append(t)
            
    for t2 in t1:
        if smaller % t2 == 0:
            max = t2
    
    print (max)
gcd(a,b)
            
            
    
    
            