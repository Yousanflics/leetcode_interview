# 81 runtime 最快的 solution
# // 地板除 -> (5 / 2) = 2.5 (5 // 2) = 2
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return True
            # tricky part, 从左到右找到第一个不是相同的 element 然后再按照原来的对比，这是对数组中有相同的元素进行处理的 tricky 一点
            while l < mid and nums[l] == nums[mid]:
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # targetis in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1;
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                #target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
