# find mini in rotated sorted array

from typing import List

# 一个时间复杂度是 O(nlogn)的写法就是二分

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # 恰好找到转折点
            # 转折点在右边
            if mid < right and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            # 转折点在中间
            if mid > left and nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
            return nums[left]
            