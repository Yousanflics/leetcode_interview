/*
求 x 的 n 次方，不可以使用 for 无脑循环无法过 oj，考虑使用递归，递归要考虑x的正负最后需要给到结果中
耗时更短的是 recursion 但是需要更多的额外空间

（C++整数除法向零舍入）

困惑点解答：

为什么在负指数且为奇数时的返回值里，是用 half * half / x 而不是 1/(half * half * x) 来表示呢？下面从数学意义和代码逻辑两个方面说明这个问题。

1. 从数学意义理解：
假设要计算 x^n，其中 n 是负的奇数，比如 n = -3。数学上我们知道：

x^-3 = 1 / (x^3)
如果我们已经算出了 x^(n/2)，记为 half，这里 n/2 会进行整数除法。例如 -3/2 = -1。

half = myPow(x, -1) = x^-1
那么 half * half = (x^-1)*(x^-1) = x^-2

*/

// recursion solution
class Solution {
public:
    double myPow(double x, int n) {
        //任何数的 0 次方都是 1
        if (n == 0) return 1;
        double half = myPow(x, n/2);
        if (n % 2 == 0) return half * half;
        // n 是 取余之后的结果如果 > 0 则说明是奇数次方，<0 则说明 n 是负数，求负数次方
        return n > 0 ? half * half * x : half * half / x;
    }
};

// iteration solution

class Solution {
public:
    double myPow(double x, int n) {
        double res = 1.0;
        for (int i = n; i != 0; i /= 2) {
            if (i % 2 != 0) res *= x;
            x *= x;
        }
        return n < 0 ? 1 / res : res;
    }
};
