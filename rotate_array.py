# https://leetcode.com/problems/rotate-array/discuss/895980/2-liner-python-solution-beats-99.8-time

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

s = Solution()
print(s.rotate(nums = [1,2,3,4,5,6,7], k = 3))