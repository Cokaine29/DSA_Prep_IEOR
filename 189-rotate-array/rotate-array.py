class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ## Brute with LOOP --> TLE !!!!

        # for i in range(k) :
        #     nums[:] = [nums[-1]] + nums[:-1]

        ## Brute with Duplicate -->

        # dup = []
        # k = k % len(nums)
        # dup = nums[-1 *(k) : ] + nums[:-1 *k]
        # nums[:] = dup



        ## Optimal and Correct Approach

        L = len(nums)
        if L == 1 :
            return nums
        k = k % L
        if k == 0 :
            return nums
        s = set()
        target = 0
        pick = nums[target]
        while len(s) != L :
            target = (target+k) % L
            if target not in s :
                hold = nums[target]
                nums[target] = pick
                s.add(target)
                pick = hold
            else :
                target = (target + 1) % L   
                pick = nums[target]






 
         
        
        