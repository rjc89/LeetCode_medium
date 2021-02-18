# https://leetcode.com/problems/next-permutation/discuss/781849/python-3-O(N)-solution-100-faster
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]
            return
        
        def reverse(i):
            nums[i:] = nums[i:][::-1]
            
        if len(nums) <= 1:
            return
        
        j = len(nums)-1
        while j >= 0 and nums[j -1] >= nums[j]:
            j -= 1
        j -= 1
        
        while j >= 0:
            i = j + 1
            while i < len(nums) and nums[j] < nums[i]:
                i += 1
            swap (i-1, j)
            break
            
        reverse(j+1)
        
        return

s = Solution()
print(s.nextPermutation(nums = [1,1,5]))