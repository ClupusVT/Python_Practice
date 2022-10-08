def get_unique_values(lst):
    list1 = []
    for i in lst:
        if i not in lst:
            list1.append(i)
    
    return list1

            



lst = [4,5,6,7,8,2]
