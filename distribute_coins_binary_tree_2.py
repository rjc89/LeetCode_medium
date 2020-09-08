# https://leetcode.com/problems/distribute-coins-in-binary-tree/
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/818495/Simulating-procedure-Intuitive-Solution.
class Solution:
    def __init__(self):
        self.dist = 0
        
    def dfs(self, root, depth, request, extra):
        if(not root):
            return [], []
        
        left_r, left_e = self.dfs(root.left, depth+1, request, extra)
        right_r, right_e = self.dfs(root.right, depth+1, request, extra)
        
        request = left_r + right_r
        extra = left_e + right_e
        
        if(root.val==0):
            request.append(depth)
        elif(root.val>1):
            extra.append([root.val-1, depth])
        
        if(len(request)>0 and len(extra)>0):
            while(request and extra):
                curr_r = request.pop() #lacking depth
                curr_p = extra[0]
                
                if(curr_p[0]==1):
                    extra.pop(0)
                else:
                    extra[0][0] -= 1
                    
                self.dist += (curr_p[1] - depth) + (curr_r - depth)
            
        return request, extra
    
    def distributeCoins(self, root: TreeNode) -> int:
        self.dfs(root, 0, [], [])
        return self.dist

s = Solution()
print(s.distributeCoins(TreeNode([3,0,0])))