class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        ele = nums[0]

        for k in nums :
            if ele == k :
                count += 1 
            else :
                count -= 1
                if count == 0 :
                    ele = k
                    count += 1
        return ele  
        