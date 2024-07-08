class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        #initialize the array to have all 0's and be n+1 in length
        dp = [0] * (n + 1)  # Initialize dp array
    
        #loop from i=2 to n+1, finding minimum cost of starting from 2 steps back or 1
        #dp contains a running total of each step
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[n]  # Minimum cost to reach the top