#Day 52 - Hash Table


#Implement a hash table.

class HashNode:
    """A node in the linked list for handling collisions."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=10):
        """Initialize the hash table with a fixed capacity."""
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):
        """Compute the hash index for a given key."""
        return hash(key) % self.capacity

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        node = self.table[index]

        # Check if the key already exists and update the value
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next

        # Insert a new node at the head of the chain
        new_node = HashNode(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def get(self, key):
        """Retrieve a value by its key."""
        index = self._hash(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None  # Key not found

    def delete(self, key):
        """Remove a key-value pair from the hash table."""
        index = self._hash(key)
        node = self.table[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                return True  # Key deleted
            prev = node
            node = node.next

        return False  # Key not found

    def display(self):
        """Display the contents of the hash table."""
        for i, node in enumerate(self.table):
            print(f"Bucket {i}:", end=" ")
            current = node
            while current:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next
            print("None")

# Example Usage
hash_table = HashTable()

hash_table.insert("name", "Alice")
hash_table.insert("age", 25)
hash_table.insert("city", "Kathmandu")

print("Initial Table:")
hash_table.display()

print("\nValue for 'name':", hash_table.get("name"))
hash_table.insert("name", "Bob")
print("\nAfter updating 'name':")
hash_table.display()

hash_table.delete("age")
print("\nAfter deleting 'age':")
hash_table.display()
