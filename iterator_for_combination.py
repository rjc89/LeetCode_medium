# def complement_oper():
#     for i in range(10):
#         print(i, ~i)

# for i in range(10):
#     print(i, ~i)

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
