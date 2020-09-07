# https://leetcode.com/problems/distribute-coins-in-binary-tree/
from typing import List
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        moves = 0
        def _dist(n):
           
            nonlocal moves                        #https://stackoverflow.com/questions/1261875/python-nonlocal-statement
            l = _dist(n.left) if n.left else 0
            r = _dist(n.right) if n.right else 0
            n.val += (l + r)
            moves += abs(n.val - 1)
            return n.val - 1
        
        _dist(root)
        return moves

s = Solution()
print(s.distributeCoins(TreeNode([3,0,0])))