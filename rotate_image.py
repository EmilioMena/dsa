"""
LC 48
runtime beats 99%
memory beats 78.19%
"""

"""
Notes:
To rotate an n x n matrix counterclockwise,
1. transpose
2. flip on y axis
"""

class Solution(object):
    def rotate(self, matrix):
        self.transpose(matrix)
        self.flip(matrix)
        
    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def flip(self, matrix):
        ncol = len(matrix[0])
        for j in range(ncol // 2):
            for i in range(len(matrix)):
                matrix[i][j], matrix[i][-1 - j] = matrix[i][-1 - j], matrix[i][j]