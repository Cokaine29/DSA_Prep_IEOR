# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.ans = float("-inf")
        def fun(root) :
            
            if not root :
                return 0 
                
            left = fun(root.left)
            right = fun(root.right)
            ele = root.val
            count = ele + max(0,left) + max(0,right) 
            self.ans = max(self.ans, count)
            
            return max(0, left, right) + ele
            
        fun(root)
        
        return self.ans
            
            