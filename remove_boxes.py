# https://leetcode.com/problems/remove-boxes/discuss/1027079/Python-implementation.
from typing import List
import functools

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @functools.lru_cache(None)
        def solve(left, right, k):
            if left > right:
                return 0
            if left == right:
                return (k + 1) ** 2
            
            trim_idx = left
            cnt = 1
            while trim_idx + 1 <= right and boxes[trim_idx] == boxes[trim_idx + 1]:
                cnt += 1
                trim_idx += 1
                
            res = solve(left + cnt, right, 0) + ((k + cnt) ** 2)
            
            for i in range(left + cnt, right + 1):
                if boxes[i] == boxes[left]:
                    res = max(res, solve(left + cnt, i - 1, 0) + solve(i, right, k + cnt))
            return res
        
        return solve(0, len(boxes) - 1, 0)
                
s = Solution()
print(s.removeBoxes(boxes = [1,3,2,2,2,3,4,3,1]))                