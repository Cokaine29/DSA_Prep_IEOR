# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:

        q = collections.deque()
        q.append(root)
        NullHit = False
        while q :
            ele = q.popleft()

            if not ele :
                NullHit = True
                continue 
            if NullHit :
                return False 
            q.append(ele.left)
            q.append(ele.right)

        return True
        