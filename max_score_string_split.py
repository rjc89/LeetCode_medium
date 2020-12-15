# https://leetcode.com/problems/maximum-score-after-splitting-a-string/discuss/597859/Linear-time-Python-solution-with-explanation

class Solution:
    def maxScore(self, s: str) -> int:
        score = max_ = s[1:].count('1') + (1 if s[0] == '0' else 0)
        for i in range(1, len(s)-1):
            score += 1 if s[i] == '0' else -1
            max_ = max(score, max_)
            
        return max_