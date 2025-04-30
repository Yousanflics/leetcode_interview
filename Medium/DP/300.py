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
    

    # 新 solution dp+二分查找(NlogN)
    def lengthOfLISBetter(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # tails[i]表示长度为i+1的递增子序列的结尾元素的最小可能值
        tails = []
        # 二分的目的：
        # 为当前处理的元素num找到 tails 数组中第一个大于等于它的位置，记为left
        for num in nums:
            # 二分查找确定插入的位置
            left, right = 0, len(tails)
            while left < right:
                # 地板除向下取整
                mid = (left+right) // 2
                if tails[mid] < num:
                    left = mid+1
                else:
                    right = mid
            # 如果 num 大于所有 tails 中的值，则添加它
            if left == len(tails):
                tails.append(num)
            else:
                # 否则替换替换第一个大于等于 num 的值
                tails[left] = num
        return len(tails)

