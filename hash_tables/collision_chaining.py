class Node:
    """A node for the linked list used in separate chaining."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Pointer to the next node

class HashTableChaining:
    """Hash table using separate chaining to handle collisions."""
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """Simple hash function."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert key-value pair, handling collisions with separate chaining."""
        index = self._hash(key)
        if self.table[index] is None:
           self.table[index] = Node(key, value)  # No collision
        else:
            # Collision: Use linked list chaining
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value  # Update existing key
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)  # Append new node

    def get(self, key):
        """Retrieve value for a given key."""
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  # Key not found
    
    def __str__(self):
        """Return a string representation of the hash table."""
        result = []
        for i, node in enumerate(self.table):
            chain = []
            while node:
                chain.append(f"{node.key}: {node.value}")
                node = node.next
            if chain:
                result.append(f"Index {i}: " + " -> ".join(chain))
        return "\n".join(result) if result else "HashTable is empty"

# Example usage
ht = HashTableChaining()
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("banana1", 20)
ht.insert("banana3", 20)
ht.insert("banana2", 20)
ht.insert("banana5", 20)
ht.insert("banana6", 20)
ht.insert("banana7", 20)
ht.insert("banana8", 20)
ht.insert("banana9", 20)
ht.insert("banana10", 20)
ht.insert("banana12", 20)
ht.insert("banana13", 20)
ht.insert("banana14", 20)
ht.insert("banana15", 20)
ht.insert("banana16", 20)
ht.insert("banana17", 20)
ht.insert("banana18", 20)
ht.insert("banana19", 19)
ht.insert("grape", 30)
ht.insert("apple", 50)  # Update value
print(ht.get("apple"))  # Output: 50
print(ht.get("banana19"))  # Output: 19
print(ht)  
