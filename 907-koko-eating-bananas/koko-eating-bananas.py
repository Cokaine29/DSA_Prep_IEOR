import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        k = r 

        while l <= r :
            mid = (l+r) // 2 
            count = 0
            for ele in piles :
                count += math.ceil(ele / mid) 
            if count <= h :
                k = min(k,mid)
                r = mid - 1
            else :
                l = mid + 1 
        return k 
        