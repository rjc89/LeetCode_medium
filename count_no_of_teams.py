#https://leetcode.com/problems/count-number-of-teams/discuss/724711/Easiest-Code-Ever-Python-Top-97-Speed-O(-n-log-n-)-Combinatorial

from sortedcontainers import SortedList

def count_high_low(sl, x):
    lo = sl.bisect_left(x)
    hi = len(sl) - sl.bisect_right(x)

    return lo, hi

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = 0
        left = SortedList()
        right = SortedList(rating)
        for x in rating:
            right.remove(x)
            loL, hiL = count_high_low(left, x)
            loR, hiR = count_high_low(right, x)
            result += loL * hiR + hiL*loR
            left.add(x)
            
        return result