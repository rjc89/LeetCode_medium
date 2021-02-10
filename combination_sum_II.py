# https://leetcode.com/problems/combination-sum-ii/discuss/961224/Python-easy-DFS-beating-95.50
from typing import List

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        
        def dfs (idx, path, target):
            if idx > len(nums):
                return
            if target == 0:
                ans.append(path)
                
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                if nums[i] > target:
                    return
                dfs(i+1, path+[nums[i]], target - nums[i])
        dfs(0, [], target)
        
        return ans
                
s = Solution()
print(s.combinationSum2(nums = [10,1,2,7,6,1,5], target = 8))