# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        self.ans = 0 
        def path(root, count) :
            if not root :
                return 
            count = count*10 + root.val


            if not root.left and not root.right :
                self.ans += count

            path(root.left, count)
            path(root.right, count)
        path(root, 0)
        return self.ans
        