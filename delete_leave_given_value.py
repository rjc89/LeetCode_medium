# https://leetcode.com/problems/delete-leaves-with-a-given-value/discuss/526084/python-greater90-short-(6-lines)-and-easy-explained

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root:
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)
            if root.val == target and not root.left and not root.right:
                root = None
        return root
