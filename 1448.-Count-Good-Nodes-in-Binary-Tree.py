# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfsGood(root, maxi):
            if not root:
                return 0  # Return 0 for an empty tree
            
            count = 0
            
            # Check if the current node is a good node
            if root.val >= maxi:
                count += 1
                maxi = root.val  # Update the maximum value encountered
            
            # Recursively check left and right subtrees
            count += dfsGood(root.left, maxi)
            count += dfsGood(root.right, maxi)
            
            return count

        return dfsGood(root, root.val)