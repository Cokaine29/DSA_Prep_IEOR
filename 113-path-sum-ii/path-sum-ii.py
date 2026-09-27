# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        self.ans = []

        def fun(root, count, nums) :
            if not root :
                return
            count += root.val
            nums.append(root.val)   
            if not root.left and not root.right :
                if count == targetSum :
                    
                    self.ans.append(nums[:])
            
            fun(root.left, count, nums)
            fun(root.right, count, nums)
            
            nums.pop()
            
            count -= root.val
            return  
           
            
            
        fun(root, 0, []) 
        
        return self.ans
                    
            
            
            

        
        