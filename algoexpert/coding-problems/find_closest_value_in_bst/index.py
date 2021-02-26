# SOLVED
def findClosestValueInBst(tree, target):
    min_value = tree.value
    head = tree
    min_diff = abs(min_value - target)

    while head is not None:
        head_value = head.value
        current_diff = abs(head_value - target)        

        if current_diff < min_diff:
            min_value = head_value
            min_diff = current_diff

        if target < head_value:
            head = head.left
        elif target > head_value:
            head = head.right
        else:
            return head.value
        
    return min_value


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


n1 = BST(10)
n1.left = BST(5)
n1.right = BST(15)


print(findClosestValueInBst(n1, 4))