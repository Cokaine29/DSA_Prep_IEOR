class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 1 :
            return 1 

        prev = -101
        ind = 0 
        for i in range(L) :
            if nums[i] == prev :
                pass 
            else :
                prev = nums[i]
                nums[ind] = prev
                ind += 1
        return ind 
                 
        