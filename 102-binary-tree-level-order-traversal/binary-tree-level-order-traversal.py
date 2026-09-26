# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root :
            return []
        q = collections.deque()
        
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
                    
            res.append(temp)
            
        return res
                
            
         

        





# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         # res = []
#         # q = collections.deque()
#         # q.append(root)

#         # while q :
#         #     qlen = len(q)
#         #     level = []
#         #     for i in range(qlen) :
#         #         node = q.popleft()
#         #         if node :
#         #             level.append(node.val)
#         #             q.append(node.left)
#         #             q.append(node.right)
#         #     if level :
#         #         res.append(level)
#         # return res  

        