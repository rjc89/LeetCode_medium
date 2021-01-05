# https://leetcode.com/problems/stone-game-ii/discuss/851536/beat-100-intuitive-code-with-explanation

class Solution:
    def stoneGameII(self, piles):
        a = [*accumulate(piles[::-1])][::-1]

        @lru_cache(None)
        def game(i, m): 
            if i + 2 * m >= len(piles): 
                return a[i]
            _minScore = 2**31 - 1  

            for x in range(1, 2 * m + 1):
                score = game(i + x, x) if x > m else game(i + x, m)
                if score < _minScore: _minScore = score
            return a[i] - _minScore
            
        return game(0, 1)