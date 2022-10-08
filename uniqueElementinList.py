def uniqueElement(list):
    list1 = []
    
    for i in list:
            while (list.count(i) > 1):
                list.remove(i)
                #print(list)
            
    
    list.sort()
    print(list)
    result = "The list of unique number is {0}"
    print(result.format(list))


uniqueElement([1,2,3,3,3,3,4,5,3,5,7,1,2,4,5,1,2,3,4,6,8,9,2,3,4,1,2])