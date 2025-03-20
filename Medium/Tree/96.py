# Unique Binary Search Tree
# Can be easily solved by DP
class Solution:
    def numTrees(self, n: int) -> int:
        """
        :type n : int
        :rtype: int
        """  
        dp = [0]*(n+1)
        dp[0] = 1
        #each n
        for x in range(1, n+1):
            #each possible root
            for y in range(1, x+1):
                dp[x] += dp[y-1]*dp[x-y]
        return dp[n]
