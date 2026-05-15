class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp={}
        dp[0]=0
        for i in range(1,amount+1):
            dp[i]=float('inf')
            for j in range(len(coins)):
                if coins[j]<=i:
                    dp[i]=min(dp[i],1+dp[i-coins[j]])
        return dp[amount] if dp[amount]!=float('inf') else -1