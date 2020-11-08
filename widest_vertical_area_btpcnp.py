#https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
from typing import List
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = sorted(x for x, y in points); max_dist = 0
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if max_dist < diff: 
                max_dist = diff
        
        return max_dist

s = Solution()
s.maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]])
        