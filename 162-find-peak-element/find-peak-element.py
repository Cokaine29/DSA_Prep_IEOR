class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return 0 

        l = 0
        r = len(nums) - 1 

        if nums[l] > nums[l+1] :
            return l
        elif nums[r] > nums[r-1] :
            return r 

        l += 1
        r -= 1

        while l <= r :
            mid = (l+r) // 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1] :
                return mid
            elif nums[mid + 1] > nums[mid] :
                l = mid + 1
            else :
                 r = mid - 1
        return -1
