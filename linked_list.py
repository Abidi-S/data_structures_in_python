# Linked list implementation in python

class Node:
    """Each Node contains the data, and the reference to the next Node"""
    def __init__(self, data):
        """Initializes a Node object"""
        self.data = data    # Assigns data
        self.next = None    # Intialize next prop as null

class LinkedList:
    """Linked list implemented as class, containing
    a reference to the Node class"""

    def __init__(self):
        """Initializes a Linked List object"""
        self.head = None
        # Value is null until explicitly assigned a Node instance

    # Traversal:
    def print_list(self):
        """Prints created linked list"""
        node = self.head
        while (node):
            print(node.data)
            node = node.next

# Construction of a simple linked list with 3 nodes
if __name__ == '__main__':

    # Empty linked list
    simple_linked_list = LinkedList()

    # Assign a value to head of linked list
    simple_linked_list.head = Node(1)

    # Two more nodes
    second_node = Node(2)
    third_node = Node(3)

    # Link first node with second
    simple_linked_list.head.next = second_node

    # Link second node with third
    second_node.next = third_node

# Thus, all three nodes are now appropriately linked
simple_linked_list.print_list()