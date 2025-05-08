# 每次可以 1 或者 2 本质是 fib 数列

"""
Fib 数列
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
结果: 0, 1, 1, 2, 3, 5, 8, 13...

爬楼梯
climbStairs(1) = 1  (爬1阶有1种方法)
climbStairs(2) = 2  (爬2阶有2种方法：1+1 或 2)
climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)
结果: 1, 2, 3, 5, 8, 13, 21...
climbStairs(n) = fib(n+1)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        # 这里返回 b 本质就是返回 fib(n+1)
        return b
