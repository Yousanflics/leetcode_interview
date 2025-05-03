# max product subarray

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = current_max = current_min = nums[0]

        for num in nums[1:]:
            candidates = (num, num*current_max, num*current_min)
            current_max, current_min = max(candidates), min(candidates)
            res = max(res, current_max)
        return res
