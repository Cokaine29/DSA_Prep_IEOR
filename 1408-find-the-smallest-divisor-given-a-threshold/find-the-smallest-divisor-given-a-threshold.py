import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        l = 1 
        r = max(nums) 
        ans = max(nums)
        while l <= r :
            mid = (l+r) // 2
            count = 0 
            for ele in nums :
                count += math.ceil(ele/mid)
            if count > threshold : 
                l = mid + 1
            else :
                ans = mid
                r = mid - 1
        return ans


