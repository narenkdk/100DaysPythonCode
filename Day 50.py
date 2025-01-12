#Day 50 - Linked List

#Implement a linked list.

class Node:
    """A class to represent a single node in a linked list."""
    def __init__(self, data):
        self.data = data  # The data held by the node
        self.next = None  # Pointer to the next node


class LinkedList:
    """A class to represent a singly linked list."""
    def __init__(self):
        self.head = None  # The first node of the linked list

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None

    def append(self, data):
        """Add a node with the given data to the end of the linked list."""
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            return
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a node with the given data to the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete the first node with the specified data."""
        if self.head is None:  # If the list is empty
            print("The list is empty.")
            return

        # If the head node is to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return

        # Search for the node to delete
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        # If the node was found, remove it
        if current.next:
            current.next = current.next.next
        else:
            print(f"Node with data {data} not found.")

    def display(self):
        """Print all the elements in the linked list."""
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display()  # Output: 10 -> 20 -> 30 -> None

    ll.prepend(5)
    ll.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

    ll.delete(20)
    ll.display()  # Output: 5 -> 10 -> 30 -> None

    ll.delete(40)  # Node with data 40 not found.
