class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()


    # Add/Append a node at the end of the linked list

    def add(self, data):
        new_node = node(data)
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    
    # The length count of the linked list

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next
        return total

    # Display the linked list

    def display(self):
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
        print (elems)



    # PLAY AROUND WITH THE FUNCTIONS

    # my_list = linked_list()

    # my_list.display()

    # my_list.add(1)
    # my_list.add(2)

    # my_list.display()



    # Extractor function / Get
    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None


        current_index = 0
        current_node = self.head.next


        while current_node != None:
            if current_index == index:
                return current_node.data
            current_node = current_node.next
            current_index += 1

        return None


# PLAY AROUND WITH THE FUNCTIONS

# my_list = linked_list()

# my_list.add(1)
# my_list.add(2)
# my_list.add(3)
# my_list.add(4)

# my_list.display()

# print ("Element at 2nd index: %d" % my_list.get(2))


# Erase a Node at a certain Index

def erase(self, index):
    if index >= self.length():
        print("ERROR: 'Erase' Index out of range")
        return

    current_index = 0
    current_node = self.head

    while True:
        last_node = current_node
        current_node = current_node.next

        if current_index == index:
            last_node.next = current_node.next
            return
        current_index += 1

# my_list = linked_list()

# my_list.add(1)
# my_list.add(2)
# my_list.add(3)
# my_list.add(4)

# my_list.display()

# my_list.erase(1)

# my_list.display()