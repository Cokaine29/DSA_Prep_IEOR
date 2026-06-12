class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        L = len(nums)

        if L == 1 :
            return nums[0]

        if nums[0] != nums[1] :
            return nums[0]
        elif nums[-1] != nums[-2] :
            return nums[-1]

        left = 1
        right = L - 2

        while left <= right :
            mid = (left + right) // 2 
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]  :
                return nums[mid]
            if mid % 2 == 0 and nums[mid + 1] == nums[mid] :
                left = mid + 1 
            elif mid % 2 == 1 and nums[mid - 1] == nums[mid] :
                left = mid + 1 
            else :
                right = mid - 1 


        