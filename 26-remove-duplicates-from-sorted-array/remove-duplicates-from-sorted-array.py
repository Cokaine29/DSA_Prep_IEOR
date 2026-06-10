class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # L = len(nums)
        # if L == 1 :
        #     return 1 

        # prev = -101
        # ind = 0 
        # for i in range(L) :
        #     if nums[i] == prev :
        #         pass 
        #     else :
        #         prev = nums[i]
        #         nums[ind] = prev
        #         ind += 1
        # return ind 

        ## Easier to look 

        L = len(nums)

        if L == 1 :
            return 1 
        i = 0 

        for j in range(1,L) :
            if nums[i] != nums[j] :
                i += 1 
                nums[i] = nums[j]
        return i + 1 
                 
        