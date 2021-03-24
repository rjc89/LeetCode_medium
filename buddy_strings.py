# https://leetcode.com/problems/buddy-strings/discuss/891275/Python-Best-Simple-and-Clean-Explained-Solution-O(n)-O(1)

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return True if len(A) - len(set(A)) >= 1 else False
        
        diff = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False
                
        if len(diff) != 2:
            return False
        
        if A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
            return True
        
        return False

s = Solution()
print(s.buddyStrings(A = "ab", B = "ba"))        