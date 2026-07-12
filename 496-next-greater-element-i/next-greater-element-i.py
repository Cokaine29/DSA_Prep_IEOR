class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:


        ans = [-1] * len(nums2)

        stack = []
        d = {}
        for i in range(len(nums2)) :
            if stack and nums2[i] > nums2[stack[-1]]:
                while stack and nums2[stack[-1]] < nums2[i] :
                    t = stack.pop()
                    ans[t] = nums2[i]
                    d[nums2[t]] = nums2[i]
            stack.append(i)
        
        ans = []
        for ele in nums1 :
            if ele not in d :
                ans.append(-1) 
            else :
                ans.append(d[ele])

        return ans



        