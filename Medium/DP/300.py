# longest increase substring

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1]*n
        # i 是当前元素
        for i in range(1, n):
            # j 是之前的元素
            for j in range(i):
                # 只有当前元素比之前的元素要大所以才会是递增的
                if nums[i] > nums[j]:
                    # 满足条件下，可能有两种 1.j结尾的加上当前元素+1 2.每次取最大，所以要跟现有的 dp[i] 进行对比
                    dp[i] = max(dp[i], dp[j] + 1)
        # dp[i] 对应的是 i 结尾的元素的最大的长度，所以找 dp 中的最大的那个数对应的就是最大长度
        return max(dp)
