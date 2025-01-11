#Day 49 - Binary Search Tree


#Implement a binary search tree.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)
        # If the key already exists, do nothing (BST does not allow duplicates)

    def search(self, key):
        """Search for a key in the BST."""
        return self._search(self.root, key)

    def _search(self, current, key):
        if current is None:
            return False  # Key not found
        if current.key == key:
            return True  # Key found
        if key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right, key)

    def in_order_traversal(self):
        """Perform in-order traversal and return a list of keys."""
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, current, result):
        if current:
            self._in_order_traversal(current.left, result)
            result.append(current.key)
            self._in_order_traversal(current.right, result)


# Example usage
bst = BinarySearchTree()
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    bst.insert(key)

print("In-order Traversal:", bst.in_order_traversal())  # Should print sorted order
print("Search for 40:", bst.search(40))  # Should return True
print("Search for 25:", bst.search(25))  # Should return False
