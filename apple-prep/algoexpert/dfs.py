# Do not edit the class below except
# for the depthFirstSearch method.
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

    def depthFirstSearch(self, array):
        array.append(self.name)
        if len(self.children) <= 0:
            return

        for child_node in self.children:
            child_node.depthFirstSearch(array)

        return array

A = Node("A")
B = A.addChild("B")
C = A.addChild("C")
D = A.addChild("D")

result_list = []
print(A.depthFirstSearch(result_list))

