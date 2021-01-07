# https://leetcode.com/problems/rectangle-area/discuss/665532/Python-sol-by-math-w-Hint

from typing import List

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        left_bound = max(A, E)
        right_bound = min(C, G)
        top_bound = min(D, H)
        bottom_bound = max(B, F)
        
        area_1 = (C - A) * (D - B)
        area_2 = (G - E) * (H - F)
        
        if (left_bound < right_bound) and (bottom_bound < top_bound):
            intersection = (right_bound - left_bound) * (top_bound - bottom_bound)
            
        else:
            intersection = 0
            
        return area_1 + area_2 - intersection

s = Solution()
print(s.computeArea(A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2))