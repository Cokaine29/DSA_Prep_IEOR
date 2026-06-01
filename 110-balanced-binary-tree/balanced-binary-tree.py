# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import math
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True

        def depth(root) :
            if not root :
                return 0 
            elif not root.left and not root.right :
                return 1 
            else :
                return 1 + max(depth(root.left), depth(root.right))  

        lh = depth(root.left)
        rh = depth(root.right)
        if abs(lh-rh) > 1 :
            return False 
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        if not left or not right :
            return False 
        return True



        
        
        
