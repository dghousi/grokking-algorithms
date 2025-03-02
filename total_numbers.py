def sum(arr):
    total = 0
    for x in arr:
        total +=x
    return total

print(sum([3, 5, 7, 9]))

def recursiveSum(arr):
    # Base case: if the array is empty, return 0
    if not arr:
        return 0
    # Recursive case: sum the first element and the sum of the rest of the array
    # arr[1:]: This slice takes all elements of the list arr starting from index 1 to the end of the list.
    # So, if arr is [3, 5, 7, 9], then:
    # arr[1:] would result in [5, 7, 9].
    return arr[0] + recursiveSum(arr[1:])
print(recursiveSum([3, 5, 7, 9]))
