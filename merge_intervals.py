# https://leetcode.com/problems/merge-intervals/discuss/953904/Python-sort.-Time%3A-O(N-log-N)-Space%3A-O(N)

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        for start, end in intervals:
            if not result or start > result[-1][1]:
                result.append([start, end])
            elif end > result[-1][1]:
                result[-1][1] = end
                
        return result

s = Solution()
print(s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))