class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0 
        j = 0 
        total = m + n 

        while j < n :
            while i<m and j<n and nums1[i] < nums2[j] :
                i += 1
            # print((i,j))
            k = total - 1 
            while k > i:
                nums1[k] = nums1[k-1]
                # print(nums1)
                k -= 1
            nums1[i] = nums2[j]
            # print(nums1)
            m += 1 
            j += 1
        