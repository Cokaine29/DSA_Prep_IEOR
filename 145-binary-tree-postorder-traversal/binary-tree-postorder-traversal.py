# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root :
        #     return []

        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        

        stack1 = []
        stack2 = []
        if root : 
            stack1.append(root)
        else : 
            return []
        while stack1 :
            node = stack1.pop()
            stack2.append(node)
            if node.left :
                stack1.append(node.left)
            if node.right :
                stack1.append(node.right)

        res = []
        for i in range(len(stack2)-1,-1,-1) :
            res.append(stack2[i].val)
        return res



        