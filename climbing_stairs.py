# https://leetcode.com/problems/climbing-stairs/discuss/998650/Easy-python-solution
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         c1, c2, c3 = 0, 1, 2
#         while n > 2:
#             c1, c2 = c2, c3
#             c3 = c1 + c2
#             n -= 1
#         return c3

# https://leetcode.com/problems/climbing-stairs/discuss/861147/Clean-Python-or-Fibonacci-Growth    
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 0
        for _ in range(n):
            a, b = a+b, a
        return a

s = Solution()
print(s.climbStairs(n = 12))