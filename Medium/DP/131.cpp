class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> out;
        helper(s, 0, out, res);
        return res;
    }

    void helper(string s, int start, vector<string>& out, vector<vector<string>>& res) {
        if(start == s.size()) { res.push_back(out); return; }
        for(int i = start; i < s.size(); ++i) {
            // 这里的 continue 是跳过上面的 for 循环，如果不是回文就不递归了
            if(!isPalindrome(s, start, i)) continue;
            out.push_back(s.substr(start, i - start + 1));
            helper(s, i + 1, out, res);
            out.pop_back();
        }
    }

    bool isPalindrome(string s, int start, int end) {
        while(start < end) {
            if(s[start] != s[end]) return false;
            ++start; --end;
        }
        return true;
    }
};

/*
一般 continue 的使用场景
continue 主要用于跳过当前循环的剩余部分，直接进入下一次循环，常见使用场景包括：

1. 过滤不符合条件的数据

for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) continue;  // 跳过偶数
    cout << i << " ";          // 输出奇数
}

输出

1 3 5 7 9

*/
