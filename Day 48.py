#Day 48 - Queues


#Implement a queue data structure.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the size of the queue."""
        return len(self.items)

    def front(self):
        """Return the front element without removing it."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Front from empty queue")

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.front())    # Output: 2
print(queue.size())     # Output: 2
