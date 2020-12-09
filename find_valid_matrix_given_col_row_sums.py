# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/discuss/876904/Python-and-C%2B%2B-(Greedy)-Easy-python-solution.-Explained-using-images
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        c, r = len(colSum), len(rowSum)
        mat = [[0 for i in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                rsum, csum = rowSum[i], colSum[j]
                min_ = min(rsum, csum)
                mat[i][j] = min_
                rowSum[i] -= min_
                colSum[j] -= min_
        
        return mat