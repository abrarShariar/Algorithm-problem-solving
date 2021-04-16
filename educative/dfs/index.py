class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum_val):
    if root is None:
        return False

    # if the root is pointing to none => leaf => return
    # this is a leaf node
    if root.val == sum_val and root.left is None and root.right is None:
        return True

    sum_val -= root.val
    # if there is a root left => dfs on it
    return has_path(root.left, sum_val) or has_path(root.right, sum_val)


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)

#   dfs(root, 23)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


main()
