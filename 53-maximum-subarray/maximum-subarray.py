class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        maxi = -1 * 2**31

        count = nums[i]

        while i < len(nums) and j < len(nums) :
            if count > maxi :
                maxi = count 
            if count <= 0 :
                j += 1
                i = j
                if i < len(nums) :
                    count = nums[i]
            else :
                j += 1 
                if j < len(nums) :
                    count += nums[j]

        return maxi

            

                

        