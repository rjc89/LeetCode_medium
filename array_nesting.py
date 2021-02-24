# https://leetcode.com/problems/array-nesting/discuss/700169/Python-Solution-using-DFS-O(N)-approach
from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        S = [set() for _ in range(len(nums))]
        vis = [False] * len(nums)
        ans = float('-inf')
        for i in range(len(nums)):
            j = i
            while not vis[j]:
                S[i].add(nums[j])
                vis[j] = True
                j = nums[j]
            ans = max(ans, len(S[i]))
        return ans

s = Solution()
print(s.arrayNesting(nums = [5,4,0,3,1,6,2]))        