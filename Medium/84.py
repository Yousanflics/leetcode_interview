# 单调栈问题
# Largest Rectangle in Histogram
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            # 这个时候需要入栈的不是单调的，比栈顶元素要大
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, w*h)
            stack.append(i)
        heights.pop()
        return ans
