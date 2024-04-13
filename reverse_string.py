##This python practice trying to reverse the string###
def reverse_string(string):
    list = []
    for c in string:
        list.append(c)
    list.reverse()
    new_string = ""
    for d in list:
        new_string = new_string + d
    
    print (new_string)
    
reverse_string("asdadsczxc")

    
    
    
    
    
