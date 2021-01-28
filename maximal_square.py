# https://leetcode.com/problems/maximal-square/discuss/518951/Python-O(m*n)-sol.-by-DP.-with-Demo
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp_table = [[int(x) for x in row] for row in matrix]
        h, w = len(matrix), len(matrix[0])
        max_edge_of_square = 0
        for y in range(h):
            for x in range(w):
                if y and x and int(matrix[y][x]):
                    dp_table[y][x] = 1 + min(dp_table[y][x-1], dp_table[y-1][x-1], dp_table[y-1][x])
                max_edge_of_square = max(max_edge_of_square, dp_table[y][x])
                
        return max_edge_of_square**2

s = Solution()
print(s.maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))