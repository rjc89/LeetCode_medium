# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0

        def dfs(root, even_grandparent, parent_val):
            if root == None:
                return

        if even_grandparent:
            self.num += root.val
        
        even_grandparent = (parent_val % 2) == 0
        dfs(root.left, even_grandparent, root.val)
        dfs(root.right, even_grandparent, root.val)

        dfs(root, False, 1)
        print(self.sum)
        return self.sum

s = Solution()
s.sumEvenGrandparent(root = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5])