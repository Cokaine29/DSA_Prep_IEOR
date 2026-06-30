class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        # i = 0 
        # j = 1 

        # while i < len(nums) and j < len(nums) :
        #     while i < len(nums) and nums[i] > 0 :
        #         i += 2 
        #     while j < len(nums) and nums[j] < 0 :
        #         j += 2 
        #     if i >= len(nums) or j >= len(nums) :
        #         break
        #     if nums[i] < 0 and nums[j] > 0 :
        #         nums[i] , nums[j] = nums[j] , nums[i]
        #     i += 2 
        #     j += 2 

        # return nums


        ans = [0] * len(nums)

        posi = 0 
        neg = 1 

        for i in range(len(nums)) :
            if nums[i] > 0 :
                ans[posi] = nums[i]
                posi += 2 
            elif nums[i] < 0 :
                ans[neg] = nums[i]
                neg += 2
        return ans
            
            


 


            
        