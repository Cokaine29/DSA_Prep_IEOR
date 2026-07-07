class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0 
        r = len(nums) - 1 
        store = 10000
        while l <= r :
            mid = (l+r) // 2 
            if nums[mid] >= nums[l] : # left sorted
                store = min(store,nums[l])
                l = mid + 1 
            else : # right sorted
                store = min(store,nums[mid])
                r = mid - 1
        return store


        