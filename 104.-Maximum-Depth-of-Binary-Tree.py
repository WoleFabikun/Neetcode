# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left,right) + 1

# At each recursive step the max depth of the left and right subtree is 
# calculated and the max of the two is returned + 1 for the current node.


# Iterative solution
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0

    stack = [[root,1]]
    res = 1

    while stack:
      node, depth = stack.pop()

      if node:
        res = max(res,depth)
        stack.append([node.left, depth + 1])
        stack.append([node.right, depth + 1])
    
    return res
