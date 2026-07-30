class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1 :
            return x 
        i = 1 

        j = x // 2 
        save = -1 
        while i <= j :
            mid = (i+j) // 2 
            if mid * mid == x :
                return mid
            elif mid * mid > x :
                j = mid - 1
            else :
                save = mid
                i = mid + 1

        return save
        