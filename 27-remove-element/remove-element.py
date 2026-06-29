class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0 
        j = len(nums) - 1
        while i <= j :
            while j > -1 and nums[j] == val :
                j -= 1
            while i < len(nums) and nums[i] != val :
                i += 1
            if i >= j :
                break
            if nums[i] == val :
                nums[i] , nums[j] = nums[j] , nums[i]
                print(nums)
                i += 1 
                j -= 1 
        return j + 1 
        