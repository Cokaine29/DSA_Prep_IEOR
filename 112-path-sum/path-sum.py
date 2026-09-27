# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        self.ans = False
        
        def fun(root, count) :
            if not root :
                return 
            count += root.val
            
            if not root.left and not root.right :
                if count == targetSum :
                    self.ans = True
            
            fun(root.left, count)
            fun(root.right, count)
            
        fun(root,0)
        return self.ans


        
        
        
        
            
        
        
        