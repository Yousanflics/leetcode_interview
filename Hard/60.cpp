/*
这个题目是需要实现查找全排列的第 K 个排序
思路：
- 利用阶乘确定每个位置的数字块大小，每个块包含的排列数位剩余位数的阶乘
比如说：
第一个数字决定“块”：如果第一个数字是1，后面两个数字的排列有2! = 2种（即一个“块”的大小是2）。同理，第一个数字是2或3时，各自对应一个大小为2的块。

每个块的排列数 = 剩余位数的阶乘：比如第一个位置确定后，剩余两位的排列数是2! = 2
*/
class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> fact(n+1, 1);
        for(int i = 1; i <= n; i++) {
            fact[i] = fact[i-1] * i;
        }

        vector<char> nums;
        for(int i = 1; i <= n; i++) {
            nums.push_back(i + '0');
        }
        string res;
        --k;

        for(int i = 0; i < n; i++) {
            int idx = k / fact[n - 1 - i];
            res += nums[idx];
            nums.erase(nums.begin() + idx);
            k %= fact[n - 1 - i];
        }
        return res;
    }
};
