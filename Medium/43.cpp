class Solution {
public:
    string multiply(string num1, string num2) {
        string res;
        int m = num1.size(), n = num2.size();
        //结果长度不会超过 m + n
        vector<int> vals(m+n); // 初始化每一位应该都为 0
        // 两个数相乘进行遍历得到的结果分别是对应的位置应该是 [i+j+1],[i+j]
        // 因为数组的最后面的才是计算的个位数所以从 size() - 1 开始遍历到 0
        for(int i = m - 1; i >=0 ; --i) {
            for(int j = n - 1; j >= 0; --j) {
                // 由于本身是字符串需要变成数字 - '0' 
                int mul = (num1[i] - '0') * (num[j] - '0');
                // vals 是结果容器，p2是进位（或者说是重复的那一位）
                int p1 = i + j, p2 = i + j + 1, sum = mul + vals[p2];
                // p1是更高的位 p2是低位 故 p1 是有多少个进位 p2 是进位之后的结果
                vals[p1] += sum/10;
                vals[p2]  = sum%10;
            }
        }
        // 对结果容器进行一个便利 如果 res 非空或者 val ！=0即res是非空或有数据就给结果中
        // 加入 val + '', val 是 int 数字
        for(int val : vals) {
            if(!res.empty() || val != 0) res.push_back(val + '0');
        }
        //如果 res 为空返回 "0" 否则返回 res 本身结果 string
        return res.empty() ? "0" : res;
    }
};
