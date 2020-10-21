from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        mid = -(-len(deck) // 2)
        #first_idx = mid -1
        main_chunk = deck[:mid]
        endpiece = deck[mid:]
        answer = []
        idx = 0
        for i in range(len(deck)):
            if i % 2 == 0:
                answer[i] = main_chunk[idx]
                idx += 1
            else:
                answer[i] = endpiece[idx]
                idx += 1
        return answer


s = Solution()
print(s.deckRevealedIncreasing([17,13,11,2,3,5,7]))
