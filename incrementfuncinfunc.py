def increment(number):
    def inner_increment():
        nonlocal number
        return number + 1
    return inner_increment()

print(increment(10))