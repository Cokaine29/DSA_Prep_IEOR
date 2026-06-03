class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        right = len(nums) - 1
        left = 0 

        while right >= left :
            mid = (left+right) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                right = mid - 1
            else :
                left = mid + 1
        
        return left 
        