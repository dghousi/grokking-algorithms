def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2  # Use integer division
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# Test the function
# my_list = [1,2,3,4,5,6,7,8,9,10]
my_list = list(range(1, 128))
print(binary_search(my_list, 127))  # Should print the index of 5
print(binary_search(my_list, -1))  # Should print None