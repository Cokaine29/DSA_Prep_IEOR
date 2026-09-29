# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        
        self.prev = None 
        self.ans = True
        def fun(root) :
            if not root :
                return None 
            fun(root.left)
            ele = root.val 
            if self.prev is not  None and ele <= self.prev :
                self.ans = False
            self.prev = ele
            fun(root.right)
            return 
        fun(root)
        return self.ans