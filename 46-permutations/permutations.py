class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if not nums :
            return [[]]
        elif len(nums) == 1 :
            return [nums]

        ans = self.permute(nums[1:])
        final = []

        for ele in ans :    # ans = [[2,3],[3,2]]
            for i in range(len(ele) + 1) :
                temp = ele[:i] + [nums[0]] + ele[i:]
                final.append(temp)
        return final
                

                

        