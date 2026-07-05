class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ## Brute
        # for i in range(len(matrix)) :
        #     for j in range(len(matrix[0])) :
        #         if matrix[i][j] == 0 :
        #             for k in range(len(matrix)) :
        #                 if matrix[k][j] == 0 :
        #                     pass
        #                 else :
        #                     matrix[k][j] = "s" 
        #             for k in range(len(matrix[0])) :
        #                 if matrix[i][k] == 0 :
        #                     pass
        #                 else :
        #                     matrix[i][k] = "s"
        # for i in range(len(matrix)) :
        #     for j in range(len(matrix[0])) :
        #         if matrix[i][j] == "s" :
        #             matrix[i][j] = 0
        # return

        ## Better

        # row = []
        # col = []

        # for i in range(len(matrix)) :
        #     for j in range(len(matrix[0])) :
        #         if matrix[i][j] == 0 :
        #             row.append(i)
        #             col.append(j)

        # for ele in row :
        #     matrix[ele][:] = [0] * len(matrix[0])
        # for ele in col :
        #     for j in range(len(matrix)) :
        #         matrix[j][ele] = 0
        # return
                    
        ## Optimal 
        row0 = False
        col0 = False
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] == 0 :
                    if i == 0 :
                        row0 = True
                    if j == 0 :
                        col0 = True

                    matrix[0][j] = "a"
                    matrix[i][0] = "a"
        
        for k in range(1,len(matrix)) :
            if matrix[k][0] == "a" :
                matrix[k][:] = [0] * len(matrix[0])
        for k in range(1,len(matrix[0])) :
            if matrix[0][k] == "a" :
                for m in range(len(matrix)) :
                    matrix[m][k]= 0

        if row0 :
            matrix[0] = [0] * len(matrix[0])
        if col0 :
            for i in range(len(matrix)):
                matrix[i][0] = 0
        return




 
        
      