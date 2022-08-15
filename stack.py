# Stack implementation in python

class Stack():
    """Stack implemented as a list with the nth
    element of the list at the top of the stack"""

    def __init__(self):
        """Creates new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items) # empty list is false-y

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        "Get the value of the top item in the stack"
        return self._items[-1]

    def size(self):
        """Get the number of items in the stacks"""
        return len(self._items)