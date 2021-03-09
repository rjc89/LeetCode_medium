# https://leetcode.com/problems/interval-list-intersections/discuss/828650/Python-two-pointer-beats-98
from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a, b = 0, 0
        res = []
        while a < len(A) and b < len(B):
            maxi = max(A[a][0], B[b][0])
            mini = min(A[a][1], B[b][1])
            if maxi <= mini:
                res.append([maxi, mini])
            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1
        
        return res

s = Solution()        
print(s.intervalIntersection(A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]))