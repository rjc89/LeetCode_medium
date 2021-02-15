# https://leetcode.com/problems/set-matrix-zeroes/discuss/856080/Simple-Python-solution-beats-99.36
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zeroi = []
        for i in matrix:
            temp = [index for index, z in enumerate(i) if z == 0]
            zeroi.append(temp)
        for index, i in enumerate(zeroi):
            if i != []:
                matrix[index] = [0] *len(matrix[0])
                for j in i:
                    for k in matrix:
                        k[j] = 0

s = Solution()
print(s.setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]]))                        