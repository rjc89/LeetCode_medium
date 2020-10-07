# Definition for a binary tree node.

# https://leetcode.com/problems/find-mode-in-binary-search-tree/
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        stack,letter,res = [],{},[]
        if not root:
            return []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val not in letter:
                    letter[root.val] = 1
                else:
                    letter[root.val] += 1
                root = root.right
        max_val=max(letter.values())
        result=[] 
        for key in letter.keys(): 
            if letter[key]==max_val: 
                result.append(key) 
        return result

s = Solution()
print(s.findMode(TreeNode([1,None,2,2])))
        