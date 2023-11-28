class Node:
    """
    An object for storing a single node in a linked list

    data: Data stored in node
    next_node: Reference to next node in the linked list

    """

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data


class SinglyLinkedList:

    """
    Linear data structure that stores values in nodes

    head: The head node of the list
    """

    def __init__(self):
        self.head = None
        self.__count = 0

    def is_empty(self):
        """
        Determines if linked list is empty. Takes 0(1) time
        """
        return self.head is None

    def __len__(self):
        """
        Returns the length of the linked list. Takes n 0(1) time
        """
        return self.__count