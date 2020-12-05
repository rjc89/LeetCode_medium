# https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/305779/python-BFS

from typing import List


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        q = root and [root]
        res = []
        while q:
            res.append(max([node.val for node in q]))
            q = [leaf for node in q for leaf in (node.left, node.right) if leaf]
        print(res)
        return res

s = Solution()
s.largestValues([1,3,2,5,3,None,9])

