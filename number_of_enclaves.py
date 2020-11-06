# https://leetcode.com/problems/number-of-enclaves/
from typing import List

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        visited = set()

        def dfs(i, j):
            if (i, j) in visited:
                return 
            visited.add((i, j))

            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j +dj
                if 0 <= ni < M and 0 <= nj < N and A[ni][nj]:
                    dfs(ni, nj)

            for i in range(M):
                for j in range(N):
                    if (i == 0 or i == M -1 or j == 0 or j == N -1) and A[i][j]:
                        dfs(i, j)
        print(sum(sum(row) for row in A) - len(visited))
        return sum(sum(row) for row in A) - len(visited)

s = Solution()
s.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])