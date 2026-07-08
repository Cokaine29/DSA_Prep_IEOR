import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        l = 1 
        r = max(nums) 
        s = 0 

        while l <= r :
            mid = (l+r) // 2
            count = 0 
            for ele in nums :
                count += math.ceil(ele/mid)
            s = min(s,count)

            if count > threshold : 
                l = mid + 1
            else :
                r = mid - 1

        print([l,r])

        return l



