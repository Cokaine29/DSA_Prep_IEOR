class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        

        stack = []
        ans = [-1] * 2 * len(nums)
        for i in range(2 * len(nums)) :
            while stack and nums[stack[-1]] < nums[i%len(nums)] :
                t = stack.pop()
                ans[t] = nums[i%len(nums)]
            stack.append(i%len(nums))


        return ans[:len(nums)]
