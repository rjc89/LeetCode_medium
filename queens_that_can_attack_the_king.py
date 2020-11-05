#https://leetcode.com/problems/queens-that-can-attack-the-king/
from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        queens = {(i, j) for i, j in queens}
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in range(1, 8):
                    x, y = king[0] + i * k, king[1] + j * k
                    if (x, y) in queens:
                        res.append([x, y])
                        break
        print(res)
        return res
s = Soltuion()
s.queensAttacktheKing(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0])