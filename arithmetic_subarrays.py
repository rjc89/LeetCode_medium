# https://leetcode.com/problems/arithmetic-subarrays/discuss/909120/python3-using-set-no-sort-O(MN)
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArith(n):
            set_n = set(n)
            if len(n) != len(set_n):
                return len(set_n) == 1

            max_, min_ = max(n), min(n)
            if (max_ - min_) % (len(n) -1) != 0:
                return False

            step = (max_ - min_)//(len(n) - 1)
            for i in range(min_, max_, step):
                if i not in set_n:
                    return False
            return True
        
        return [isArith(nums[start:stop+1]) for start, stop in zip(l, r)]