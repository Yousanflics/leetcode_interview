from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0]*(n + 1)
        ans = 0
        #通过遍历 二维数组 对每一类的高度get到对应的高度，捕获到了高度之后拿到 height 的数据然后变成了 84 题
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h*w)
                stack.append[i]
        return ans
