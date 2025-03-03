
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([]))
print(quicksort([10]))
print(quicksort([10,5,2,3]))
print(quicksort([1,5,2,3]))
print(quicksort([7800,45,450,78,456,988,12,10,56,1]))
print(quicksort([10,8,2,4,1]))
print(quicksort([10,18,21,41,11]))