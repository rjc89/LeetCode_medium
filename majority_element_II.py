# https://leetcode.com/problems/majority-element-ii/discuss/858881/Python-simple-and-clear-solution-O(n)-time-O(1)-space
from typing import List
from collections import defaultdict 

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_dict = defaultdict(int)
        for n in nums:
            my_dict[n] += 1
            if len(my_dict) == 3:
                dic = defaultdict(int)
                for key, val in my_dict.items():
                    if val > 1:
                        dic[key] = val - 1
                
                my_dict = dic
                
        return [n for n in my_dict.keys() if nums.count(n) > len(nums) / 3]

s = Solution()
print(s.majorityElement(nums = [3,2,3]))