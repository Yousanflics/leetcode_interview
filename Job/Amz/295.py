# 295 寻找数据流中的中位数
"""
这道题的理解：需要我们设计一个数据结构，支持 1.添加整数到数据流 2.随时放回当前所有数据中的中位数
中位数的定义：如果元素的个数是奇数，中卫市所有数排序后的中间值；如果个数是偶数，中位数是中间两个数的平均值

思路分析：
可以采用“两个堆”的巧妙办法：1.一个大堆 small 存储较小的一半数字，2.一个小堆 large 存储较大的一半数字，并且
保持 small 和 large 的大小差不超过 1，这样的话中位数就会是：
如果两个堆大小相同：两个对应元素的平均值
如果大小不同，元素多的那个堆顶的元素

python heapq 默认只提供最小堆，但是这里还需要一个最大堆所以
large: 直接使用最小堆，堆顶是最小元素
small: 通过从存储元素的负值，将最最小堆变成最大堆，堆顶是最大元素的负值
因此， small 堆顶的 -small[0] 是较小数据中的最大值，large[0] 是较大一半数据中的最小值

python 中 heapq.pushpop(heap, item) 是一个原子操作，比先 push 再 pop 要好很多
"""

import heapq

class MedianFinder:
    def __init__(self):
        self.small = [] # the smaller half of the list, max heap (invert min-heap)
        self.large = [] # the larger half of the list, min heap

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            #两个堆大小相等的时候，让 large 多一个元素
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            # large 比 small 多一个元素（因为相等的时候让 large 比 small 多了一个），所以把 num 加入 large 后弹出 targe 的对应元素，取反加入 small 堆保证两个堆的平衡
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        # 两个堆大小相同的时候取 large 的堆顶和 small 的堆顶取反
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        # 不想定的话，根据上面的算法一定是 large 比 small 多，因为相等的时候是让 large 多一个元素，所以直接取 large 的堆顶就好了
        else:
            return float(self.large[0])
