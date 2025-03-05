# 4.7 Doubling the value of just the first element in an array (O(1))
def double_first_element(arr):
    if arr:  # Ensure the array is not empty
        arr[0] *= 2
    return arr

arr = [2, 3, 7, 8, 10]

print(double_first_element(arr)) 
