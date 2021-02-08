# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/discuss/368490/Python-o(n)-time-O(1)-memory-with-explanation
from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        zig, zag = 0, 0
        prev_zig, prev_zag = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            if i % 2 == 0:
                zig += max(0, prev_zig - nums[i] + 1)
                prev_zig = nums[i]
                zag += max(0, nums[i] - prev_zag + 1)
                prev_zag = nums[i] - max(0, nums[i] - prev_zag + 1)
                
            else:
                zag += max(0, prev_zag - nums[i] + 1)
                prev_zag = nums[i]
                zig += max(0, nums[i] - prev_zig + 1)
                prev_zig = nums[i] - max(0, nums[i] - prev_zig + 1)
        
        return min(zig, zag)

s = Solution()
print(s.movesToMakeZigzag(nums = [1,2,3]))