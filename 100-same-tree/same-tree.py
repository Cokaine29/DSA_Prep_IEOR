# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p,q) :
            if not p and q :
                return False 
            elif not q and p :
                return False
            elif not p and not q :
                return True
            if p.val != q.val :
                return False
            lt = dfs(p.left, q.left)
            rt = dfs(p.right, q.right)

            return lt and rt

        return dfs(p,q)

            



        