# recursive
# solved

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current_node = self.root
        new_node = Node(new_val)
        self.insert_helper(current_node, new_node)
        
    
    def insert_helper(self, current_node, new_node):
        if new_node.value >= current_node.value:
            if current_node.right == None:
                current_node.right = new_node
                return
            self.insert_helper(current_node.right, new_node)
        else:
            if current_node.left == None:
                current_node.left = new_node
                return
            self.insert_helper(current_node.left, new_node)
            

    def search(self, find_val):
        current_node = self.root
        return self.search_helper(current_node, find_val)
    
    def search_helper(self, current_node, find_val):
        
        if current_node == None:
            return False
            
        elif current_node.value == find_val:
            return True
        
        elif find_val > current_node.value:
            return self.search_helper(current_node.right, find_val)
            
        else:
            return self.search_helper(current_node.left, find_val)
        
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)