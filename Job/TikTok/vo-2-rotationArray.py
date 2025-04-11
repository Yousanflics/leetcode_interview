# 在旋转数组中搜索

def search(nums, target):
    """
    在旋转排序数组中搜索目标zhi
    参数:
        nums: 旋转后的排序数组
        target: 要搜索的目标值
    
    返回:
        如果找到目标值，返回其下标，否则返回 -1
    """
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
    
# 测试案例
test_cases = [
    ([4, 5, 6, 7, 0, 1, 2], 0),  # 返回 4
    ([4, 5, 6, 7, 0, 1, 2], 3),  # 返回 -1
    ([1], 0),                    # 返回 -1
    ([1, 3], 3),                 # 返回 1
    ([4, 5, 6, 7, 8, 1, 2, 3], 8)  # 返回 4
]

for nums, target in test_cases:
    print(f"数组: {nums}, 目标值: {target}, 结果: {search(nums, target)}")
            
