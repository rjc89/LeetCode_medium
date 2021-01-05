# https://leetcode.com/problems/spiral-matrix/discuss/999388/95.41-faster-solution
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        while matrix:
            result += matrix.pop(0)
            matrix = (list(zip(*matrix)))[::-1]
            
        return result
        
s = Solution()
print(s.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))

# 