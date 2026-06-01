# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root : 
    #         return 0 
    #     if not root.left and not root.right :
    #         return 1 
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # BFS way
        if not root :
            return 0
        res = []
        q = collections.deque()
        q.append(root)    

        while q :
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                level.append(node.val)
                if node and node.left :
                    q.append(node.left)
                if node and node.right :
                    q.append(node.right)
            res.append(level)
        return len(res)