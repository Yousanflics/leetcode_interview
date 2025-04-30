# minimium meeting rooms
import heapq
# python 中默认是最小堆

# 为什么这题需要使用最小堆：
# - 需要一种数据结构来追踪当前所有正在进行的会议的结束时间
# -能够快速找到最早结束的会议（以便决定是否可以复用会议室）

# 优先队列特性：
# - heapq 实现了最小堆，它能确保堆顶元素始终是所有元素中的最小值
# - 对于我们的问题来说，这意味着堆顶元素就是最早结束的会议时间
# - 当新会议开始时，我们只需要检查这个最早结束的会议是否已经结束

# 考察用最小堆，优先队列
class Solution:
    def minMeetingRooms(intervals):
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        # 最小堆
        rooms = []
        # 第一个会议的结束时间
        heapq.heappush(rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            #后续开始的时间在之前结束的时间之后说明可以复用会议室，先弹出堆顶，然后将当前会议的结束时间加入堆中
            # 每次把没有入栈的 interval 跟栈顶的对比（因为是最早结束的）
            if intervals[i][0] >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])
        # 堆的大小就是需要的会议室数量
        return len(rooms)
    
# 使用 heapq 构造最大堆 
# num = [3, 1, 5, 7, 2], max_heap = [-num for num in nums]
# heapq.heapify(max_heap), max_val = -heapq.heappop(max_heap)

"""

import heapq

def initialize_max_heap(lst):
    # 将原始列表中的元素取负值
    max_heap = [-x for x in lst]
    # 使用 heapify 将列表转换为堆
    heapq.heapify(max_heap)
    return max_heap

# 使用示例
lst = [4, 1, 7, 3, 8, 5]
max_heap = initialize_max_heap(lst)

# 如果需要弹出最大元素
max_value = -heapq.heappop(max_heap)

"""
