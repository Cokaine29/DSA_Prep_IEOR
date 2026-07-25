class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        ans = 0
        tens = 0 
        a , b = num1 , num2

        for i in range(len(b)-1,-1,-1) :
            temp = ""
            carry = 0 
            for j in range(len(a) - 1, -1, -1) :
                m = int(a[j]) * int(b[i])  + carry
                keep = m % 10 
                temp = str(keep) + temp 
                carry = m // 10  
            if carry :
                temp = str(carry) + temp
            ans += int(temp) * 10**tens
            tens += 1 
       
        return str(ans)




    
        