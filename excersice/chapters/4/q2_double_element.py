# 4.6 Doubling the value of each element in an array (O(n))
def double_elements(arr):
    for i in range(len(arr)):
        arr[i] *= 2
    return arr

# Example array
arr = [2, 3, 7, 8, 10]

print(double_elements(arr)) 
