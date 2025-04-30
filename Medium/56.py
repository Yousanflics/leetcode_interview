#56 merge intervals
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # 一定要首先基于第一个下标进行排序，否则不能使用后面的算法
        intervals.sort(key=lambda x: x[0])
        # 这里记得写中括号，不然不好对比
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            #处理当前区间
            current = intervals[i]
            previous = merged[-1]
            # overlapped
            if current[0] <= previous[1]:
                previous[1] = max(current[1], previous[1])
            else:
                merged.append(current)
            
        return merged

