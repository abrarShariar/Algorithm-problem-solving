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
        head = self
        is_set = False
        node = BST(value)

        while not is_set:
            if node.value >= head.value:
                if head.right is None:
                    head.right = node
                    is_set = True
                else:
                    head = head.right
            else:
                if head.left is None:
                    head.left = node
                    is_set = True 
                else:
                    head = head.left

        return self

    def contains(self, value):
        if self.value == value:
            return True
        head = self
        node = BST(value)
        while head:
            if node.value > head.value:
                head = head.right
            elif node.value < head.value:
                head = head.left
            else:
                return True

        return False

    def remove(self, value):
        # find the node required to remove
        # if the node has left subtree 
            # get the max node 
        # if the node has right subtree
            # get the min node in the ruight subtree
        node_to_del = self.search_node(value)
        head = node_to_del
        is_removed = False
        while not is_removed:
            if node_to_del.left:
                # find the 


    def get_min(self, node):
        


    def search_node(self, value):
        head = self
        node = BST(value)
        while head:
            if node.value < head.value:
                head = head.left
            elif node.value > head.value:
                head = head.right
            else:
                return node

        return None

bst = BST(10)
bst.insert(5)
bst.insert(15)
bst.insert(13)
bst.insert(22)



print(bst.remove(15))

