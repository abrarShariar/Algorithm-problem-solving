# # This is the class of the input root. Do not edit it.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# def branchSums(root):
#     # Write your code here.
#     pass


# # DFS preorder traversal
# def depthFirstSearch (head, currentSum, resultList):
#     currentSum += head.value

#     if head.left:
#         depthFirstSearch(head.left, currentSum, resultList)

#     if head.right:
#         depthFirstSearch(head.right, currentSum, resultList)
    
#     resultList.append(currentSum)
#     return resultList



# n1 = BinaryTree(1)
# n1.left = BinaryTree(2)
# n1.right = BinaryTree(3)
# n1.left.left = BinaryTree(4)
# n1.left.left.left = BinaryTree(8)

# print(depthFirstSearch(n1, n1.value, []))

# SOLVED

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    result_list = []
    running_sum = 0
    getBranchSums(root, result_list, running_sum)
    return result_list


def getBranchSums(node, result_list, running_sum):
    if node is None:
        return

    running_sum += node.value

    if node.left is None and node.right is None:
        result_list.append(running_sum)
        return

    getBranchSums(node.left, result_list, running_sum)
    getBranchSums(node.right, result_list, running_sum)
    

bt = BinaryTree(1)
bt.left = BinaryTree(2)
bt.right = BinaryTree(3)
bt.left.left = BinaryTree(4)

print(branchSums(bt))
