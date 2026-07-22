class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        def back(i,stack,count) :
            if count == target :
                ans.append(stack.copy())
                return 
            elif i >= len(candidates) or count > target :
                return 
            
            stack.append(candidates[i])
            back(i,stack,count + candidates[i])
            stack.pop()
            back(i+1,stack,count)

        back(0,[],0)

        return ans

        