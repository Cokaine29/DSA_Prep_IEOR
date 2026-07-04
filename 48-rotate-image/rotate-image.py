class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        

        def transpose(matrix) :
            for i in range(len(matrix)) :
                for j in range(len(matrix[i])) :
                    if i < j :
                        matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j] 
            return matrix

        matrix = transpose(matrix)

        for i in range(len(matrix)) :
            matrix[i][:] = matrix[i][-1::-1]

        return matrix