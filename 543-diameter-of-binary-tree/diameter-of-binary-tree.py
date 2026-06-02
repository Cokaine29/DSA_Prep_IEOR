# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0 
        def Diameter(root) :
            if not root :
                return 0
            ld = Diameter(root.left)
            rd = Diameter(root.right)
            self.maxD = max(self.maxD, ld + rd )
            return max(ld,rd) + 1 
        Diameter(root) 
        return self.maxD

        