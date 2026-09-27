# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # self.track = None
        # d = {p,q} 
        
        # def score(root,p,q) : ## --> int
        #     if not root :
        #         return 0 
        #     if root in d :
        #         khud = 1 
        #     else :
        #         khud = 0 
        #     ans = score(root.left,p,q) + score(root.right,p,q) + khud
        #     if ans == 2 and not self.track :
        #         self.track = root
        #     return ans 
        # score(root,p,q)
        # return self.track
        ## left 
        ## right 
        ## left + right + self 

        if not root :
            return None
            
        if root == p :
            return p 
        elif root == q :
            return q 
        
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        
        if left and right :
            return root
            
        return left if left else right