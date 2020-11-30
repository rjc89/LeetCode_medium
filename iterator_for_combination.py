# def complement_oper():
#     for i in range(10):
#         print(i, ~i)

# for i in range(10):
#     print(i, ~i)


#https://leetcode.com/problems/day-of-the-week/discuss/377576/Solution-in-Python-3-(beats-100.0-)-(one-line)
# from datetime import date

# class Solution:
#     def dayOfTheWeek(self, d: int, m: int, y: int) -> str:
#         return date(y,m,d).strftime("%A")

#https://leetcode.com/problems/bulb-switcher-iv/discuss/755871/Python-Greedy-O(n)
# class Solution:
#     def convertToTitle(self, n: int) -> str:
#         capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
#         result = []
#         while n > 0:
#             result.append(capitals[(n-1)%26])
#             n = (n -1) // 26

#         result.reverse()
#         return ''.join(result)

# class Solution:
#     def minFlips(self, target: str) -> int:
#         count = 0 
#         flip = '0'
#         for bulb in target:
#             if bulb != flip:
#                 count += 1
#                 flip = '1' if flip == '0' else '0'
#         return count
# https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation




# https://leetcode.com/problems/iterator-for-combination/
from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.allCombinations = list(combinations(characters, combinationLength))
        self.count = 0

    def next(self) -> str:
        self.count += 1
        return ''.join(self.allCombinations[self.count-1])

    def hasNext(self) -> bool:
        return self.count < len(self.allCombinations)
        


# Your CombinationIterator object will be instantiated and called as such:


obj = CombinationIterator("abc", 2)
param_1 = obj.next()
param_2 = obj.hasNext()
param_3 = obj.next()
param_4 = obj.hasNext()
param_5 = obj.next()
param_6 = obj.hasNext()



print(param_1 ,
param_2 ,
param_3 ,
param_4 ,
param_5 ,
param_6)
