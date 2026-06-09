class Solution:
    def check(self, nums: List[int]) -> bool:

        ## Brute

        L = len(nums) 
        if L == 1 :
            return True
        prev = nums[0]
        pivot = 0 
        for i in range(L) :
            if nums[i] < prev :
                pivot = i
                break
            prev = nums[i] 
        sorted = nums[pivot:] + nums[:pivot]
        # print(sorted)
        for i in range(1,len(sorted)) :
            if sorted[i] < sorted[i-1] :
                return False 
        return True
        