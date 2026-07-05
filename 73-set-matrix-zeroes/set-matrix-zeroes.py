class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] == 0 :
                    for k in range(len(matrix)) :
                        if matrix[k][j] == 0 :
                            pass
                        else :
                            matrix[k][j] = "s" 
                    for k in range(len(matrix[0])) :
                        if matrix[i][k] == 0 :
                            pass
                        else :
                            matrix[i][k] = "s"
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] == "s" :
                    matrix[i][j] = 0
        return
                    

        
      