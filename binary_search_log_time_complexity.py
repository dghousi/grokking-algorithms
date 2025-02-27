import time

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

# Create a list from 1 to 10
my_list = list(range(1, 10000))

# Best Case
start_time = time.time()
best_case_result = binary_search(my_list, 1)  # Middle element
end_time = time.time()
print(f"Best Case Result: {best_case_result}, Time Taken: {end_time - start_time:.10f} seconds")

# Worst Case
start_time = time.time()
worst_case_result = binary_search(my_list, 999)  # Element not in the list
end_time = time.time()
print(f"Worst Case Result: {worst_case_result}, Time Taken: {end_time - start_time:.10f} seconds")