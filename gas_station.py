# https://leetcode.com/problems/gas-station/discuss/860347/Python-simple-and-very-short-explained-solution-O(n)-O(1)-faster-than-98

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(gas) - sum(cost) < 0):
            return -1
        
        gas_tank, start_index = 0, 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i+1
                gas_tank = 0
                
        return start_index

s = Solution()
print(s.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))