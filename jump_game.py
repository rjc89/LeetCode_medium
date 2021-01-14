# https://leetcode.com/problems/jump-game/discuss/774588/Python%3A-Easy!-Linear-Time-O(n)-and-Space-O(1)-oror-Explanation

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachableIndex = 0
        for curr in range(len(nums)):
            if curr + nums[curr] >= reachableIndex:
                reachableIndex = curr + nums[curr]
            if curr == reachableIndex:
                break
                
        return reachableIndex >= len(nums) - 1

s = Solution()
print(s.canJump(nums = [2,3,1,1,4]))
