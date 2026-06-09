class Solution:
    def check(self, nums: List[int]) -> bool:

        ## Brute

        # L = len(nums) 
        # if L == 1 :
        #     return True
        # prev = nums[0]
        # pivot = 0 
        # for i in range(L) :
        #     if nums[i] < prev :
        #         pivot = i
        #         break
        #     prev = nums[i] 
        # sorted = nums[pivot:] + nums[:pivot]
        # # print(sorted)
        # for i in range(1,len(sorted)) :
        #     if sorted[i] < sorted[i-1] :
        #         return False 
        # return True


        ## Optimal

        # L = len(nums)
        # if L == 1 :
        #     return True
        # count = 0 
        # # new = nums[:] + nums[:]
        # i = 0 
        # j = 1 
        # while i < 2*L and j < 2*L:
        #     while j < 2*L and nums[j % L] >= nums[(j-1) % L] :
        #         j += 1 
        #     if j - i >= L :
        #         return True
        #     else :
        #         i = j 
        #         j += 1
        # return False


        ## Optimal - Better Code

        L = len(nums)
        count = 1 
        if L == 1 :
            return True
        for i in range(1, 2*L) :
            if nums[i % L ] >= nums[(i - 1) % L] :
                count += 1 
            else :
                count = 1 
            if count == L :
                return True
        return False 

        