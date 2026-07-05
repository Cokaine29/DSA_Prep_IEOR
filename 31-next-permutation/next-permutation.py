class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1 :
            return nums
        point = -1
        for i in range(len(nums)-2,-1,-1) :
            if nums[i] < nums[i+1] :
                point = i 
                print(point)
                break
        if point == -1 :
            i = 0 
            j = len(nums) - 1
            while i < j :
                nums[i] , nums[j] = nums[j] , nums[i] 
                i += 1
                j -= 1
            return nums
        for i in range(len(nums)-1,point - 1, -1) :
            if nums[i] > nums[point] :
                nums[point] , nums[i] = nums[i], nums[point]
                break

        i = point + 1 
        j = len(nums) - 1

        while i < j :
            nums[i] , nums[j] = nums[j] , nums[i] 
            i += 1
            j -= 1
        return nums
                