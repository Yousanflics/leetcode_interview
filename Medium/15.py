# 3sum 经典双指针实现

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            # 当前大于0后面都是大于 0 和不可能为 0
            if nums[i] > 0:
                break
            # 针对第一个数进行去重
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 从第三个开始，和最后一个开始找第三个
            left, right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left +=1
                elif total > 0:
                    right -=1
                else:
                    res.append([nums[i], nums[left],nums[right]])
                    # 去重第二个
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # 去重第三个
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left +=1
                    right -=1
        return res
"""
其实可以归纳一下这里的去重，之前有合并区间的题目也有去重，只要对数据的要求是唯一的不可以重复的，那么对于每一个数据
都需要去重，这里就是三个元素，那么三个元素都需要去重
"""
