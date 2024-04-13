def get_unique_values(lst):
    list1 = []
    for i in lst:
        if i not in lst:
            list1.append(i)
    
    return list1


def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False


n = int(input())
print(is_prime(n))

lst = [4,5,6,7,8,2]
