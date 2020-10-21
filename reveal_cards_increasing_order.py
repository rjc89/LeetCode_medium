from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        mid = -(-len(deck) // 2)
        #first_idx = mid -1
        answer = deck[:mid]
        for i in range(mid, (len(deck)), 1):
            for j, k in enumerate(answer):
                answer[j+1] == deck[i]


        return sorted_deck, mid


s = Solution()
print(s.deckRevealedIncreasing([17,13,11,2,3,5,7]))
