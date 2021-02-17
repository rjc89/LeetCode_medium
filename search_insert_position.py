# https://leetcode.com/problems/search-insert-position/discuss/1025719/Fast-and-simple-solution
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

s = Solution()
print(s.searchInsert(nums = [1,3,5,6], target = 5))            