#https://leetcode.com/problems/ways-to-make-a-fair-array/discuss/944521/Python3-O(N)-Simple-code-%2B-Explanation

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd_sum_r, even_sum_r = 0, 0
        odd_sum_l, even_sum_l = 0, 0
        sum_arr = []
        ans = 0
        
        for i in range(len(nums)-1, -1, -1):
            sum_arr.append([odd_sum_r, even_sum_r, odd_sum_l, even_sum_l])
            if i%2:
                odd_sum_r += nums[i]
            else:
                even_sum_r += nums[i]
                
        sum_arr = sum_arr[::-1]
        
        for i in range(len(nums)):
            sum_arr[i][2], sum_arr[i][3] = odd_sum_l, even_sum_l
            if i%2:
                odd_sum_l += nums[i]
            else:
                even_sum_l += nums[i]
                
        for i in range(len(nums) -1, -1, -1):
            if sum_arr[i][2] + sum_arr[i][1] == sum_arr[i][3] + sum_arr[i][0]:
                ans += 1
        
        
        return ans