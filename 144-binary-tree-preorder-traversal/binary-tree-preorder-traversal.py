# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root :
        #     return []
        
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


        # stack = []
        # res = []
        # stack.append(root)

        # while stack :
        #     node = stack.pop()
        #     if node :
        #         res.append(node.val)
        #     if node and node.right :
        #         stack.append(node.right)
        #     if node and node.left :
        #         stack.append(node.left)
        # return res


        res = []
        
        def preorder(root) :
            if not root :
                return 
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
            
            return 
        preorder(root)
        return res

        





        