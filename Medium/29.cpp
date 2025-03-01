// 难点在于不让使用乘法和除法要完成两数相除
// labs 是对 long 型数据的 abs， c++ 的 abs 是根据不同的数据类型返回不同的 abs 之后的数据
class Solution {
public:
    int divide(int dividend, int divisor) {
        long m = labs(dividend), n = labs(divisor), res = 0;
        if (m < n) return 0;
        long t = n, p = 1;
        while (m >= (t << 1)) {
            t <<= 1;
            p <<= 1;
        }
        res += p + divide(m - t, n);
        if ((dividend < 0) ^ (divisor < 0)) res = -res;
        return res > INT_MAX ? INT_MAX : res;
    }
};
