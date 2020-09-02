#https://leetcode.com/problems/minimum-cost-for-tickets/
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        _1day_pass, _7day_pass, _30day_pass = 0, 1, 2               # index of ticket
        NOT_Traveling_Day = -1                                      # Predefined constant to represent not-traverling day
        dp_cost = [NOT_Traveling_Day for _ in range(366)]           # DP Table, record for minimum cost of ticket to travel
        dp_cost[0] = 0                                              # base case: # no cost before travel
        for day in days:
            dp_cost[day] = 0                                            # initialized to 0 for traverling days
        for day_i in range(1, 366):                                 # Solve min cost by Dynamic Programming
            if dp_cost[day_i] == NOT_Traveling_Day:   
                dp_cost[day_i] = dp_cost[day_i - 1]                 # today is not traveling day                 # no extra cost
            else:
                dp_cost[day_i] = min(   dp_cost[ day_i - 1 ]  + costs[ _1day_pass ],                                 # today is traveling day
                                        dp_cost[ max(day_i - 7, 0) ]  + costs[ _7day_pass ],                    # compute optimal cost by DP
                                        dp_cost[ max(day_i - 30, 0) ] + costs[ _30day_pass ]     ) 
        return dp_cost[365]                                                         # Cost on last day of this year is the answer
s = Solution()
print(s.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))