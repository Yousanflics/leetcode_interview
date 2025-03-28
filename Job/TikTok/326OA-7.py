import math

def getMinAdjustments(videoScores, maxAdjustments):
    # 二分查找的下界和上界
    left, right = 1, max(videoScores)
    result = right  # 初始化结果为上界
    
    while left <= right:
        mid = (left + right) // 2
        
        # 计算使用mid作为x时需要的总调整次数
        adjustments_needed = 0
        for score in videoScores:
            # 对每个分数，计算需要多少次调整（向上取整）
            adjustments_needed += math.ceil(score / mid)
        
        if adjustments_needed <= maxAdjustments:
            # 如果当前mid可行，尝试更小的值
            result = mid
            right = mid - 1
        else:
            # 如果当前mid不可行，尝试更大的值
            left = mid + 1
    
    return result


if __name__ == '__main__':
    # 测试用例 0
    videoScores_0 = [1, 2, 3]
    maxAdjustments_0 = 4
    result_0 = getMinAdjustments(videoScores_0, maxAdjustments_0)
    print(f"Test Case 0: {result_0}")  # 应该输出 2
    
    # 测试用例 1
    videoScores_1 = [4, 3, 2, 7]
    maxAdjustments_1 = 5
    result_1 = getMinAdjustments(videoScores_1, maxAdjustments_1)
    print(f"Test Case 1: {result_1}")  # 应该输出 4
    
    # 添加自定义测试用例
    try:
        print("\n输入自定义测试数据:")
        n = int(input().strip())
        videoScores = []
        for _ in range(n):
            videoScores.append(int(input().strip()))
        maxAdjustments = int(input().strip())
        
        result = getMinAdjustments(videoScores, maxAdjustments)
        print(f"自定义测试结果: {result}")
    except EOFError:
        print("输入结束")
    except Exception as e:
        print(f"输入错误: {e}")
