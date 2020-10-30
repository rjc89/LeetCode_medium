# https://leetcode.com/problems/subrectangle-queries/
from typing import List
class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        # make a new dictionary
        self.rec = {}
		# with enumerate we can iterate through the list rectangle, 
		# taking each row and its index
        for i, row in enumerate(rectangle):
			# we map each row to its index as it`s more space-efficent
            self.rec[i] = row

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
		# we want to put new value from row1 to row2, so we iterate through them
        for i in range(row1, row2+1):
			# we put new value only from col1 to col2, but we leave other columns as is
            self.rec[i] = self.rec[i][:col1] + [newValue]*(col2-col1+1) + self.rec[i][col2+1:]

    def getValue(self, row: int, col: int) -> int:
		# take row (of type list) from dictionary rec, take specified col from row
        return self.rec[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

obj = SubrectangleQueries([[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]])
obj.updateSubrectangle(0, 0, 2, 2, 5)
param_2 = obj.getValue(3, 1)