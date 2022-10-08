def my_function_max(*number):
    max = 0
    for i in number:
        
        if i >= max:
            max = i
    
    print(max)
            
my_function_max(5,9,123123,123213)
        
        