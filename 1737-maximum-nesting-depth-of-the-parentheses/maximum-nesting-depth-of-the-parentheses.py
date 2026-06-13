class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        count = 0  
        ans = 0
        for ele in s :
            if ele == "(" :
                stack.append(ele)
                count = len(stack)
                ans = max(count,ans)
            elif ele == ")" : 
                stack.pop()
        return ans 
            
        