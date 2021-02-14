# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        
        # if the value is greater than current node value => go right
        if value > self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BST(value)

        # if the value is less than the current node value => go left
        else:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BST(value)

        return self

    def contains(self, value):
        if self.value == value:
            return True
        
        if self.left is not None:
            self.left.contains(value)

        if self.right is not None:
            self.right.contains(value)

        return False


    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        # keep going right till we find the largest
        # this is a leaf nod


def depth_first_traverse(root_node):
    if root_node is None:
        return

    print(root_node.value)
    depth_first_traverse(root_node.left)
    depth_first_traverse(root_node.right)
    
bst = BST(10)
bst.insert(12)
bst.insert(1)
bst.insert(2)
bst.insert(3)

print(bst.contains(100))
print(bst.contains(10))
print(bst.contains(1))



# depth_first_traverse(bst)
