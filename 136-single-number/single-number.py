class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        L = len(nums)

        if L == 1 :
            return nums[0]
        
        ans = nums[0]

        for i in nums[1:] :
            ans = ans ^ i

        return ans 