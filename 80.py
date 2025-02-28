from typing import List
class Solution:
    def removeDulicaptes(self, nums: List[int]) -> int:
        if(len(nums) < 3):
            return len(nums)
        pos = 2
        #肯定是从2以上开始，只有2个就直接保留了
        for i in range(2, len(nums)):
            #需要注意这里后面一个是 nums[pos - 2], 这是这个算法的核心
            #也可以理解为 i 是整个nums的遍历函数，快指针，pos是允许保留的数组的部分因为是慢指针，慢指针 - 2 跟当前的快指针都不一样那说明没有重复超过两次那么就可以加入，把当前的 pos 的 index 赋值给到新可以加入的指针就到位了
            if nums[i] != nums[pos - 2]:
                nums[pos] = nums[i]
                pos += 1
        return pos
    
# test code
sol = Solution()
nums = [1, 1, 1, 2, 2, 3]
length = sol.removeDulicaptes(nums)
print(length)
print(nums[:length])
