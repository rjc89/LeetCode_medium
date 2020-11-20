# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         ans = []
#         max_candy = max(candies)
#         for i, j in enumerate(candies):
#             if j+extraCandies >= max_candy:
#                 ans.append([True])
#             else:
#                 ans.append(False)
#         return ans

# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         first = nums[:n]
#         second = nums[n:]
#         ans = []
#         for i in range(0,n,1):
#             ans.append(first[i])
#             ans.append(second[i])
        
#         return ans
# https://leetcode.com/problems/make-sum-divisible-by-p/

from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p
        if not remainder:
            return 0
        ans = float('inf')
        presum = [0]
        remainders = {0: -1}
        for i, n in enumerate(nums):
            presum.append(presum[-1] + n)
            r = ((cr := presum[-1] % p) - remainder) % p
            if r in remainders:
                ans = min(ans, i - remainders[r])
            remainders[cr] = i
        return ans if ans < len(nums) else -1

s = Solution()
s.minSubarray(nums = [6,3,5,2], p = 9)
    