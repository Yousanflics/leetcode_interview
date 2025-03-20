# Unique Binary Search Tree
# Can be easily solved by DP
"""
这个问题的关键是理解：当我们选择某个数作为根节点时，比它小的数都会在左子树，比它大的数都会在右子树
"""
class Solution:
    def numTrees(self, n: int) -> int:
        """
        :type n : int
        :rtype: int
        """  
        # 创建长度为 n+1 且初始化为 0 的 dp 数组 dp[n+1]
        # 计算 0 到 n 个节点能组成的书的数量
        dp = [0]*(n+1)
        dp[0] = 1 #空树 也是一种情况所以 dp[0] = 1
        #each n
        # 计算每个 dp[x]  的值，这里的 x 表示当前我们要计算的节点数量
        for x in range(1, n+1):
            #each possible root
            # 当有 x 个节点的时候 1-x 中的每一个都可能是根节点，y表示我们选择的根节点
            for y in range(1, x+1):
                # Important！！！:状态转移方程，
                # 左子树有 y-1个节点（1 到 y-1），右子树有 x-y 个节点（y+1 到 x）
                # 左子树可能的结构数量是 dp[y-1] 右子树的结构数量是 dp[x-y]，根据乘法原则，左右子树组合的总数量是 dp[y-1]* dp[x-y]
                dp[x] += dp[y-1]*dp[x-y]
        return dp[n]
