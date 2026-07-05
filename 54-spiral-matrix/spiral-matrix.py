class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m , n = len(matrix) , len(matrix[0])
        top = 0 
        bottom = m - 1
        left = 0
        right = n - 1
        ans = []
        ## Method 1
        # def spiral(matrix,top,bottom,left,right,ans) :
        #     if left <= right :
        #         for i in range(left,right+1) :
        #             ans.append(matrix[top][i])
        #         top += 1
        #     if top <= bottom :
        #         for i in range(top,bottom+1) :
        #             ans.append(matrix[i][right])
        #         right -= 1
        #     if left <= right and top <= bottom:
        #         for i in range(right,left - 1,-1) :
        #             ans.append((matrix[bottom][i]))
        #         bottom -= 1
        #     if top <= bottom and left <= right:
        #         for i in range(bottom, top - 1,-1) :
        #             ans.append(matrix[i][left])
        #         left += 1
        #     return top,bottom,left,right,ans
        # while left <= right and top <= bottom : 
        #     top,bottom,left,right,ans = spiral(matrix,top,bottom,left,right,ans)
        # return ans


        ## Method 2 

        while top <= bottom and left <= right :
            # top left --> top right 
            for i in range(left,right+1) :
                ans.append(matrix[top][i])
            top += 1
            # top right --> bottom right
            if top <= bottom :
                for i in range(top,bottom+1) :
                    ans.append(matrix[i][right])
                right -= 1 
            # bottom right --> bottom left
            if left <= right and top <= bottom :
                for i in range(right,left-1,-1) :
                    ans.append(matrix[bottom][i])
                bottom -= 1
            # bottom left --> top left
            if left <= right and top <= bottom :
                for i in range(bottom,top-1,-1) :
                    ans.append(matrix[i][left]) 
                left += 1


        return ans





        