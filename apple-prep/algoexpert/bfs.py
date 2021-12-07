# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
# SOLVED!
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        node_queue = []
        node_queue.append(self)
        while len(node_queue) > 0:
            current_node = node_queue.pop(0)
            array.append(current_node.name)
            for child_node in current_node.children:
                node_queue.append(child_node)
        return array
