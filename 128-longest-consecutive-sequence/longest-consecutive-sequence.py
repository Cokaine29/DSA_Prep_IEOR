class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ## Brute 
        # if len(nums) == 0 :
        #     return 0
        # nums.sort()

        # count = 1 
        # ans = 1 
        # back = nums[0]
        # for ele in nums[1:] :
        #     if ele - 1 == back :
        #         count += 1
        #         ans = max(ans,count)
        #     elif ele == back :
        #         count = count 
        #     else :
        #         count = 1
        #     back = ele
        # return ans


        ## Optimal 

        n = len(nums) 

        if n == 0 :
            return 0 
        elif n == 1 :
            return 1 

        s = set(nums)
        
        count = 1
        ans = 1
        for ele in s :
            if ele - 1 not in s :
                count = 1 
                while ele + 1 in s :
                    count += 1 
                    ans = max(ans,count)
                    ele += 1
        return ans
                    

        