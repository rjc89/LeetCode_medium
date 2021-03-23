# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/discuss/1027839/Python3-solution-easy-to-understand
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = max(nums)
        nums.remove(max(nums))
        b = max(nums)
        return (a-1)*(b-1)

s = Solution()
print(s.maxProduct(nums = [3,4,5,2]))