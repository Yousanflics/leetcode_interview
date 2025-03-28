# def calculateTikTokShoppingCost(vouchersCount, prices):
#     if not prices or vouchersCount == 0:
#         return sum(prices)
    
#     # 创建价格的副本并排序（从大到小）
#     sorted_prices = sorted(prices, reverse=True)
    
#     # 一个更简单和准确的贪心策略
#     for _ in range(vouchersCount):
#         # 每次找到当前最大价格，并将其减半
#         max_index = 0
#         for i in range(1, len(sorted_prices)):
#             if sorted_prices[i] > sorted_prices[max_index]:
#                 max_index = i
        
#         sorted_prices[max_index] /= 2
    
#     # 计算最终成本（向下取整）
#     return int(sum(sorted_prices))

import heapq

def calculateTikTokShoppingCost(vouchersCount, prices):
    if not prices or vouchersCount == 0:
        return sum(prices)
    
    # 将价格转换为最大堆（通过存储负值来模拟最大堆）
    max_heap = [-price for price in prices]
    heapq.heapify(max_heap)
    
    # 使用折扣券
    for _ in range(vouchersCount):
        # 取出最大值
        max_price = -heapq.heappop(max_heap)
        # 减半后放回堆
        max_price /= 2
        heapq.heappush(max_heap, -max_price)
    
    # 计算最终总成本
    return int(sum(-price for price in max_heap))

if __name__ == '__main__':
    # 测试用例 0
    vouchersCount_0 = 3
    prices_0 = [8, 2, 13]
    result_0 = calculateTikTokShoppingCost(vouchersCount_0, prices_0)
    print(f"Test Case 0: {result_0}")  # 应该输出 9

    vouchersCount_1 = 3
    prices_1 = [80]
    result_1 = calculateTikTokShoppingCost(vouchersCount_1, prices_1)
    print(f"Test Case 1: {result_1}")  # 应该输出 10

    vouchersCount_2 = 5
    prices_2 = [8, 2, 13]
    result_2 = calculateTikTokShoppingCost(vouchersCount_2, prices_2)
    print(f"Test Case 2: {result_2}")  # 应该输出 12.5
    
    # 添加自定义测试用例
    # 输入格式将按照图片中的说明处理：
    # 第一行是折扣券数量
    # 第二行是商品数量
    # 后面的每一行是一个商品价格
    try:
        print("\n输入自定义测试数据 (按Ctrl+D结束输入):")
        vouchersCount = int(input().strip())
        n = int(input().strip())
        prices = []
        for _ in range(n):
            prices.append(int(input().strip()))
        
        result = calculateTikTokShoppingCost(vouchersCount, prices)
        print(f"自定义测试结果: {result}")
    except EOFError:
        pass
    except Exception as e:
        print(f"输入错误: {e}")
