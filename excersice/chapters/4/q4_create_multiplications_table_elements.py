# 4.8 Creating a multiplication table with all elements in the array (O(n^2))
def multiplication_table(arr):
    table = []
    for num1 in arr:
        row = [num1 * num2 for num2 in arr]
        table.append(row)
    return table

arr = [2, 3, 7, 8, 10]

print("\n 4.8 Multiplication table:")
table = multiplication_table(arr)
for row in table:
    print(row)