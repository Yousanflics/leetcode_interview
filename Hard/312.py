# burst ballon 经典区间 dp 题目
# 这题跟 rob house 最大的区别不是要计算 nums[left]*nums[i]*nnums[right] 最大的区别是戳破气球之后 left 和 right 就成为相邻的了
# 并且这里 nums[-1] 和 nums[n] 都是 1，乘以1本身是没啥影响的

"""
这是一个经典的动态规划问题，但思路有点特别。直观的想法是考虑哪个气球先戳破，但这会让问题变得复杂，因为戳破一个气球后，剩余气球的相邻关系会发生变化。
更好的方法是考虑哪个气球最后戳破。通过这种方式，我们可以将问题分解为独立的子问题。
"""

from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        # 初始化 dp 表
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                for i in range(left+1, right):
                    coins = nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]
                    dp[left][right] = max(dp[left][right], coins)
        return dp[0][n-1]



