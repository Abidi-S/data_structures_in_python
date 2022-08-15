# Queue implementation in python

class Queue():
    """Queue implemented as a list with the nth
    item of the list at the front of the queue"""

    def __init__(self):
        """Creates new queue"""
        self._items = []

    def is_empty(self):
        """Checks if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove an item from the front of the queue"""
        return self._items.pop()

    def size(self):
        """Get the number of items in a queue"""
        return len(self._items)
