class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        level = 0 
        ans = ""
        for ch in s :
            if ch == "(" :
                if level > 0 :
                    ans += ch
                level += 1 
            elif ch == ")" :
                level -= 1 
                if level > 0 :
                    ans += ch
                
        return ans
        