# Definition for a binary tree node.
#https://leetcode.com/problems/insert-into-a-binary-search-tree/
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
            
        else:
            root.left = self.insertIntoBST(root.left, val)
            
        return root


s = Solution()
Root_ = TreeNode([4,2,7,1,3])
s.insertIntoBST(root = Root_, val = 5)

