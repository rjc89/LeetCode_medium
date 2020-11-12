#https://leetcode.com/problems/queries-on-a-permutation-with-key/
from typing import List
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        z = [i for i in range(1+m+1)]
        x = []
        
        for i in range(0, len(queries)):
            j = z.index(queries[i])
            x.append(j)
            z.insert(0, z[j])
            z.pop(j+1)

        return x

s = Solution()
s.processQueries(queries = [3,1,2,1], m = 5)