book = {}
book['apple'] = 0.67
book['milk'] = 1.49
book['avocado'] = 1.49 
print(book)

# Get input from the user
search_item = input("Search an item: \n")

# Check if the item exists in the dictionary
if search_item in book:
    print("The item is:", search_item,", the price is:", book[search_item])
else:
    print("The item", search_item ,"is not in the dictionary!")