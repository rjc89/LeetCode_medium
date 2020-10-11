# Definition for a binary tree node.
# https://leetcode.com/problems/find-mode-in-binary-search-tree/
from typing import List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        cnts = collections.Counter()
        mv = 0
        
        def helper(node):
            nonlocal mv
            if not node:
                return
            cnts[node.val] += 1
            mv = max(mv, cnts[node.val])
            helper(node.left)
            helper(node.right)
            
        helper(root)
        return [k for k,v in cnts.items() if v == mv]

s = Solution()
print(s.findMode([1,None,2,2]))

        