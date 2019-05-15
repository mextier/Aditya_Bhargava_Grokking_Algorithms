def binary_search(list, item):
    low, hi = 0, len(list) - 1
    while low <= hi:
        mid = (low + hi) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            hi = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9,10,12,15,17]
print(binary_search(my_list,10))
