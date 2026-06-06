class Solution:
    def largestOddNumber(self, num: str) -> str: 
        L = len(num) 
        j = L - 1
        for i in range(L - 1, -1 , -1) :
            if int(num[i]) % 2 == 1 :
                break
            else :
                j -= 1 
        return num[:j+1]

         