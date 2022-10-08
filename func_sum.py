def my_function_sum(*number):
    max = 0
    for i in number:
        max = max + i
    
    print(max)
            
my_function_sum(5,9,123123,123213)
