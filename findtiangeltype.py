a = int(input())
b = int(input())
c = int(input())

if (a == b) and (a == c):
    print ("Equilateral triangle")
if (a == b) or (a == c) or ( c == b):
    print ("Isosceles triangle")
if (a != b) and (a != c) and (b != c) and (b+c >= a) and (a+c >= b) and (b+a >= c):
    print ("Scalene triangle")