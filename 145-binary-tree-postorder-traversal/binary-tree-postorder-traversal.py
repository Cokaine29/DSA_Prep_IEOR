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
        

        # stack1 = []
        # stack2 = []
        # if root : 
        #     stack1.append(root)
        # else : 
        #     return []
        # while stack1 :
        #     node = stack1.pop()
        #     stack2.append(node)
        #     if node.left :
        #         stack1.append(node.left)
        #     if node.right :
        #         stack1.append(node.right)

        # res = []
        # for i in range(len(stack2)-1,-1,-1) :
        #     res.append(stack2[i].val)
        # return res

        # Using 1 stack

        # res = []
        # stack = [root]
        # visit = [False]

        # while stack :
        #     curr , v = stack.pop() , visit.pop()
        #     if curr :
        #         if v :
        #             res.append(curr.val)
        #         else :
        #             stack.append(curr)
        #             visit.append(True)
        #             stack.append(curr.right)
        #             visit.append(False)
        #             stack.append(curr.left)
        #             visit.append(False)

        # return res

        ## All Three Traversals using only 1 stack

        preorder = []
        inorder = []
        postorder = []

        if not root :
            return []

        stack = []
        stack.append([root, 1])
        while stack :
            node = stack.pop()
            if node[1] == 1 :
                preorder.append(node[0].val)
                node[1] += 1 
                stack.append(node)
                if node[0].left :
                    stack.append([node[0].left, 1])
            elif node[1] == 2 :
                inorder.append(node[0].val)
                node[1] += 1 
                stack.append(node)
                if node[0].right :
                    stack.append([node[0].right, 1])
            elif node[1] == 3 :
                postorder.append(node[0].val)
        return postorder
                



        