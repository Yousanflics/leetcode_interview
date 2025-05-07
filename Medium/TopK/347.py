from collections import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  # 方法1：使用Counter + 排序
        # count = Counter(nums)
        # return [item[0] for item in count.most_common(k)]
        count = Counter(nums)
        
        """这种速度比上面更快"""
        # 使用最小堆，保持堆的大小为k
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 从堆中提取结果
        return [item[1] for item in heap]
