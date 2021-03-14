# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # append the current node to the array
        array.append(self.name)
        # explore all the children and call the dfs on them
        for child in self.children:
            child.depthFirstSearch(array)

        return array


A = Node("A")
A.addChild("B")
A.addChild("C")
A.addChild("D")
B = Node("B").addChild("E")

output_list = []
res = A.depthFirstSearch(output_list)
print(res)