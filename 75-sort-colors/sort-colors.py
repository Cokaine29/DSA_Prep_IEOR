class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # Approach 1  /// NOT IN PLACE

        # ans = [1] * len(nums)
        # i , j = 0 , len(nums) - 1 
        # for ele in nums :
        #     if ele == 0 :
        #         ans[i] = 0 
        #         i += 1 
        #     elif ele == 2 :
        #         ans[j] = 2 
        #         j -= 1 
        #     else :
        #         pass
        # return ans


        ## Approach 

        i,j = 0, 0
        k = len(nums) - 1 

        while j <= k :
            if nums[j] == 0 :
                nums[i] , nums[j] = nums[j] , nums[i]
                i += 1
                j += 1
            elif nums[j] == 2 :
                nums[j] , nums[k] = nums[k] , nums[j]
                k -= 1 
            else :
                j += 1






        