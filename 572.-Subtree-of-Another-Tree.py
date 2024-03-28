# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSub(p,q):
            # Base case: If both nodes are None, they are equal.
            if not p and not q:
                return True
            # If one of the nodes is None, they are not equal.
            if not p or not q:
                return False
            # Check if the current nodes have the same value.
            if p.val != q.val:
                return False
            # Recursively check the left and right subtrees.
            return isSub(p.left, q.left) and isSub(p.right, q.right)
        
        if not root:
            return False

        if root.val == subRoot.val and isSub(root,subRoot):
            return True
        
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)


            