# https://leetcode.com/problems/subtree-of-another-tree/discuss/932536/Python-DFS-traversal
#from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(node):
            def same(n1, n2):
                if not n1 and not n2:
                    return True
                if not n1 or not n2 or n1.val != n2.val:
                    return False
                return same(n1.left, n2.left) and same(n1.right, n2.right)
            
            if not node:
                return False
            if node.val == t.val and same(node, t):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(s)

s = Solution()
print(s.isSubtree(s = [3,4,5,1,2], t = [4,1,2]))        