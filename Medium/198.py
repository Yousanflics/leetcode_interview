# 198 rob house 打家劫舍

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 处理边界情况
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # dp[i] 表示偷到第 i 个房子的时候能获得的最大金额
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # 对于每个房子都有两种结果，偷还是不偷
        # - 如果偷第 i 个那么就不能偷第 i - 1 个房子，最大金额为 dp[i-2]+nums[i]
        # - 如果不偷第 i 个，那么最大金额就是偷到第 i-1 个房子的最大金额

        # 初始条件
        # - dp[0] = nums[0] ，只有一个房子的时候，直接偷
        # - dp[1] = max(nums[0], nums[1]) 有两个房子的时候选择有最多钱的那个偷
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]
