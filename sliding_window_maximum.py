#https://leetcode.com/problems/sliding-window-maximum/discuss/1058121/O(n)-Fast-and-Readable
import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
                
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
            
        return output

s = Solution()
print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))