class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1 
        ans = 0
        digit = False 
        sign = 1 
        sign_done = False
        for ele in s :
            if not ele.isnumeric() :
                if ele == " " and not digit and not sign_done:
                    pass
                elif ele == "-" and not digit and not sign_done:
                    sign = -1 
                    sign_done = True
                elif ele == "+" and not digit and not sign_done:
                    sign = +1
                    sign_done = True
                else :
                    break
            else :
                digit = True
                ans = ans * 10 + int(ele) 
                
        ans = sign * ans 
        if ans < INT_MIN :
            ans = INT_MIN
        elif ans > INT_MAX :
            ans = INT_MAX
        
        return ans
                
               

            
        