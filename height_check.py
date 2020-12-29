# https://leetcode.com/problems/height-checker/discuss/429670/Python-3-O(n)-Faster-than-100-Memory-usage-less-than-100

from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        '''function for finding the min no. of items to move in order to achieve ascending order of integers in an array'''        
        max_val = max(heights)
        
        # frequency table
        freq = [0] * (max_val + 1)
        for num in heights:
            freq[num] += 1
        for num in range(1, len(freq)):
            freq[num] += freq[num -1]
            
        # places table
        places = [0] * len(heights)
        for num in heights:
            places[freq[num]-1] = num
            freq[num] -= 1
            
        return sum([a != b for a, b in zip(heights, places)])
        
s = Solution()
s.heightChecker(heights = [1,1,4,2,1,3])