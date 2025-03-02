def sum(arr):
    total = 0
    for x in arr:
        total +=x
    return total

print(sum([1,2,3,4]))

def recursiveSum(arr):
    # Base case: if the array is empty, return 0
    if not arr:
        return 0
    # Recursive case: sum the first element and the sum of the rest of the array
    return arr[0] + recursiveSum(arr[1:])
print(recursiveSum([1,2,3,4]))
