# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    pass


# DFS preorder traversal
def depthFirstSearch (head, currentSum, resultList):
    currentSum += head.value

    if head.left:
        depthFirstSearch(head.left, currentSum, resultList)

    if head.right:
        depthFirstSearch(head.right, currentSum, resultList)
    
    resultList.append(currentSum)
    return resultList



n1 = BinaryTree(1)
n1.left = BinaryTree(2)
n1.right = BinaryTree(3)
n1.left.left = BinaryTree(4)
n1.left.left.left = BinaryTree(8)

print(depthFirstSearch(n1, n1.value, []))