class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ## Brute with LOOP --> TLE !!!!

        # for i in range(k) :
        #     nums[:] = [nums[-1]] + nums[:-1]

        ## Brute with Duplicate -->

        dup = []
        k = k % len(nums)
        dup = nums[-1 *(k) : ] + nums[:-1 *k]
        nums[:] = dup
 
         
        
        