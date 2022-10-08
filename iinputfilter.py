str = str(input())

def inputfilter(str):
    list = []
    x = str.split()
    print (x)
    for i in x:
        t1 = 0
        for t in i:
            t1 = t1+1
        if t1 >= 3 :
            list.append(i)
            
    print (list)
            
                
            

inputfilter(str)