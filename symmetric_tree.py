#https://leetcode.com/problems/symmetric-tree/discuss/939789/python-best-and-explained-O(n)-recursion

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def isMirror(tree1, tree2):
            if not tree1 or not tree2:
                return tree2 == tree1
            if tree1.val != tree2.val:
                return False
            
            return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)
        
        return isMirror(root.left, root.right)

s = Solution()
print(s.isSymmetric(root = [1,2,2,3,4,4,3]))