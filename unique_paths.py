#https://leetcode.com/problems/unique-paths/discuss/959838/12-MS-oror-EASY-oror-PYTHON-oror-RECURSION-oror-MEMOISATION-oror-DP

class Solution(object):
    def uniquePaths(self, m, n, cache = dict()):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if (m,n) in cache:
            return cache[(m,n)]
        
        if m == 1 and n == 1:
            return 1
    
        if m == 0 or n == 0:
            return 0
        
        cache[(m, n)] = self.uniquePaths(m - 1, n, cache) + self.uniquePaths(m, n - 1, cache)
        return cache[(m, n)]

s = Solution()
print(s.uniquePaths(m = 3, n = 7))        