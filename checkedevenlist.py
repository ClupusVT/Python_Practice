#Initial list
res = []

# Input lengths
print ("Print the lengths for your res:")
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)


def evenNum(res):
    evenlist = []
    for i in res:
        if i % 2 == 0:
            evenlist.append(i)
    print (evenlist)
    
evenNum(res)


    
            
