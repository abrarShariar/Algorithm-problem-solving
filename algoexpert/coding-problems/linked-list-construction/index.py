# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)
        
    def setTail(self, node):
        # find the tail first
        self.tail = self.head
        while self.tail.next is not None:
            self.tail = self.tail.next

        self.tail.next = node
        node.prev = self.tail

    def insertBefore(self, node, nodeToInsert):
        running_pointer = self.head
        while running_pointer.next != node:
            running_pointer = running_pointer.next

        nodeToInsert.prev = running_pointer
        nodeToInsert.next = running_pointer.next
        nodeToInsert.next.prev = nodeToInsert
        running_pointer.next = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        running_pointer = self.head
        while running_pointer != node:
            running_pointer = running_pointer.next

        if running_pointer.next is None:
            running_pointer.next = nodeToInsert
            nodeToInsert.prev = running_pointer
        else:
            running_pointer.next.prev = nodeToInsert
            nodeToInsert.prev = running_pointer
            nodeToInsert.next = running_pointer.next
            running_pointer.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        running_pointer = self.head
        position -= 1
        while position > 0:
            running_pointer = running_pointer.next
            position -= 1

        if running_pointer.prev is None:
            nodeToInsert.next = running_pointer
            running_pointer.prev = nodeToInsert
        else:
           nodeToInsert.next = running_pointer
           nodeToInsert.prev = running_pointer.prev
           running_pointer.prev.next = nodeToInsert
           running_pointer.prev = nodeToInsert
            
        
    def removeNodesWithValue(self, value):
        temp_head = self.head
        while temp_head is not None:
            if temp_head.value == value:
                if temp_head.next is not None:
                    temp_head.next.prev = temp_head.prev
  
                temp_head.prev.next = temp_head.next
            
            temp_head = temp_head.next

    def remove(self, node):
        running_head = self.head
        while running_head != node:        
            running_head = running_head.next
        
        if running_head.next is not None:
            running_head.next.prev = running_head.prev

        running_head.prev.next = running_head.next

    def containsNodeWithValue(self, value):
        running_head = self.head
        while running_head is not None:
            if running_head.value == value:
                return True
            running_head = running_head.next
        
        return False
