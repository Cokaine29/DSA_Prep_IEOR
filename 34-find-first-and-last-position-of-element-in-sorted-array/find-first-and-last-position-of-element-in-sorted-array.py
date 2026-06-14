class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l = -1 
        r = -1 

        left = 0 
        right = len(nums) - 1 

        while left <= right :
            mid = (left + right) // 2
            if nums[mid] == target :
                l = mid
                right = mid - 1
            elif target < nums[mid] :
                right = mid - 1 
            else :
                left = mid + 1
        
        left = 0 
        right = len(nums) - 1 
    
        while left <= right :
            mid = (left + right) // 2 
            if nums[mid] == target :
                r = mid
                left = mid + 1 
            elif target < nums[mid] :
                right = mid - 1
            else :
                left = mid + 1 

        return [l,r]
        

        