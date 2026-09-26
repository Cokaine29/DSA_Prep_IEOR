# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root :
            return []
        q = collections.deque()
        order = 1 
        q.append(root)
        while len(q) :
            l = len(q)
            temp = []
            for i in range(l) :
                ele = q.popleft()
                temp.append(ele.val)
                if ele.left :
                    q.append(ele.left)
                if ele.right :
                    q.append(ele.right)
            if order == 1 :
                res.append(temp)                
            elif order == 0 :
                res.append(temp[-1::-1])
            order = 1 - order
            
        return res
                
            
         

        



# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root :
#             return []
#         q = collections.deque()
#         q.append(root)
#         res = []
#         order = 1
#         while q :
#             qLen = len(q) 
#             level = []
#             for i in range(qLen) :
#                 node = q.popleft()
#                 level.append(node.val)
#                 if node.left :
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             res.append(level) if order == 1 else res.append(level[-1::-1])
#             order = -1 * order 
#         return res
        