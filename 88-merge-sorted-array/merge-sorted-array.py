class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ## Approach 1 
        # i = 0 
        # j = 0 
        # total = m + n 

        # while j < n :
        #     while i<m and j<n and nums1[i] < nums2[j] :
        #         i += 1
        #     # print((i,j))
        #     k = total - 1 
        #     while k > i:
        #         nums1[k] = nums1[k-1]
        #         # print(nums1)
        #         k -= 1
        #     nums1[i] = nums2[j]
        #     # print(nums1)
        #     m += 1 
        #     j += 1
        

        ## Approach 2  : O(m+n) without any extra space

        i = m - 1
        j = n - 1 
        k = m + n - 1

        while j > -1 and i > -1:
            if nums1[i] > nums2[j] :
                nums1[k] = nums1[i]
                k -= 1 
                i -= 1
            else :
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        while  j > -1 :
            nums1[k] = nums2[j] 
            j -= 1 
            k -= 1 
     
