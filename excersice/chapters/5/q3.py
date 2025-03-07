# 5.3 f(x)=next_empty_slot() | not consistent
# Consistency: This function likely returns the next available slot in some 
# data structure (like a hash table). If the state of the data structure 
# changes (e.g., if items are added or removed), the output can change. 
# Therefore, it is not consistent.

class SimpleHashTable:
    def __init__(self):
        self.table = [None] * 7  # Fixed size
        self.next_slot = 0
    
    def next_empty_slot(self):
        while self.next_slot < len(self.table) and self.table[self.next_slot] is not None:
            self.next_slot += 1
        return self.next_slot if self.next_slot < len(self.table) else None
    
    def insert(self, value):
        slot = self.next_empty_slot()
        if slot is not None:
            self.table[slot] = value
            return slot
        return None

# Example usage
hash_table = SimpleHashTable()
print(hash_table.insert("apple"))  # Output: 0
print(hash_table.insert("milk"))   # Output: 1
print(hash_table.insert("avocado")) # Output: 2
print(hash_table.insert("banana"))  # Output: 3
print(hash_table.insert("grape"))   # Output: 4
print(hash_table.insert("orange"))  # Output: 5
print(hash_table.insert("mango"))   # Output: 5
print(hash_table.insert("avocado"))  # Output: None (no empty slots)