class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def find_row(matrix,target) :
            l = 0 
            r = len(matrix) - 1 
            m = len(matrix)
            n = len(matrix[0])
            while l <= r :
                mid = (l+r) // 2
                if target >= matrix[mid][0] and target <= matrix[mid][n-1] :
                    return mid
                elif target > matrix[mid][n-1] :
                    l = mid + 1
                else :
                    r = mid - 1 
            return -1

        def search(nums,target) :
            l = 0 
            r = len(nums) - 1 
            while l <= r :
                mid = (l+r) // 2 
                if nums[mid] == target :
                    return True
                elif target > nums[mid] :
                    l = mid + 1
                else :
                    r = mid - 1
            return False 
            
        row = find_row(matrix,target)
        if row == -1 :
            return False
        ans = search(matrix[row],target)

        return ans

        
        