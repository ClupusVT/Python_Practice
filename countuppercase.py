def show(s):
    uppercase = 0
    lowercase = 0 
    for t in s:
        if t.isupper():
            uppercase = uppercase + 1
        if t.islower():
            lowercase = lowercase + 1

    print("Given string:",s)
    print("Number of uppercase letters:",uppercase)
    print("Number of uppercase lowercase:",lowercase)
    

s = str(input())
show(s)