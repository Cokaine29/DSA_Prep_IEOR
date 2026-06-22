class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 0 :
            return False
        ans = (n - 1) & n 

        if ans == 0 :
            return True
        else :
            return False 
        