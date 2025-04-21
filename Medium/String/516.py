# 最长回文子串

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # 创建二维 dp
        dp = [[0]* n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        # 填充DP表
        # 注意遍历顺序：从下到上，从左到右
        """
        dp[i][j]表示从索引i到j的最长回文子序列长度
        所以当我们从下到上遍历i（从i+1到i），从左到右遍历j（从j-1到j）时，我们可以确保：

        计算 dp[i][j] 时，其左下方的值 dp[i+1][j-1] 已经计算好
        下方的 dp[i+1][j] 已经计算好
        左方的 dp[i][j-1] 也已经计算好
        """
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
        
