def hash_function_1(input_string):
    """Return '1' for all input."""
    return 1

def hash_function_2(input_string):
    """Use the length of the string as the index."""
    return len(input_string)

def hash_function_3(input_string):
    """Use the first character of the string as the index."""
    if input_string:
        return ord(input_string[0]) - ord('a')
    return -1  # Return -1 for empty strings

def hash_function_4(input_string, hash_size=10):
    """Map every letter to a prime number and calculate the hash."""
    prime_mapping = {
        'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11,
        'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
        'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47,
        'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71,
        'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101
    }
    
    total = 0
    for char in input_string:
        if char in prime_mapping:
            total += prime_mapping[char]
    
    return total % hash_size

# Example usage
test_string = "bag"

print("Hash Function 1:", hash_function_1(test_string))
print("Hash Function 2:", hash_function_2(test_string))
print("Hash Function 3:", hash_function_3(test_string))
print("Hash Function 4:", hash_function_4(test_string))

# 5.5 Phonebook with names as keys and phone numbers as values
phonebook = {
    "Esther": "123-456-7890",
    "Ben": "234-567-8901",
    "Bob": "345-678-9012",
    "Dan": "456-789-0123"
}

# Function to display phonebook entries
def display_phonebook(phonebook):
    for name, number in phonebook.items():
        print(f"{name}: {number}")

print("Phonebook:")
display_phonebook(phonebook)

# 5.6 Mapping from battery size to power
battery_power = {
    "A": 1.5,
    "AA": 1.5,
    "AAA": 1.2,
    "AAAA": 1.2
}

# Function to display battery sizes and their corresponding power
def display_battery_power(battery_power):
    for size, power in battery_power.items():
        print(f"Battery Size {size}: {power}V")

print("\nBattery Power Mapping:")
display_battery_power(battery_power)

# 5.7 Mapping from book titles to authors
books_authors = {
    "Maus": "Art Spiegelman",
    "Fun Home": "Alison Bechdel",
    "Watchmen": "Alan Moore"
}

# Function to display book titles and their authors
def display_books_authors(books_authors):
    for title, author in books_authors.items():
        print(f"'{title}' by {author}")

print("\nBooks and Authors Mapping:")
display_books_authors(books_authors)