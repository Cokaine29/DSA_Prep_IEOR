# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def pre(root1, root2) :
            if not root1 and not root2 :
                return True
            elif not root1 and root2 :
                return False
            elif not root2 and root1 :
                return False
            if root1.val == root2.val :
                return pre(root1.left, root2.right) and pre(root1.right, root2.left)
            else :
                return False
            

        if not root :
            return True
        else :
            return pre(root.left, root.right)
        