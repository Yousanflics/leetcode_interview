// 经典 dp, 面试中多次出现

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<bool>dp(s.size() + 1, false);
        // dpi 表示前 i 个字符串是否可以用 wordDict 表示
        dp[0] = true;

        for(int i = 1; i <= s.size(); i++) {
            for(int j = 0; j < i; j++) {
                // 为什么需要 dpj? 因为 dpj 决定了前一个子状态， j=true + i = true 才能全局 true
                if(dp[j] && wordSet.count(s.substr(j, i-j))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.size()];
    }
};

/*
优化后的代码解释
循环优化：在 for (int j = 0; j < i; ++j) 内部，检查到 dp[j] 为 true 且 s[j:i] 在 wordDict 中时，立即将 dp[i] 设置为 true，然后直接 break，跳出 j 的循环。
剪枝效果：一旦 dp[i] = true，表示 s[0:i] 已经可以被成功分割，所以不需要再检查其他可能的 j 值，直接进入下一个 i。
示例
假设 s = "leetcode"，wordDict = ["leet", "code"]，在计算 dp[8] 时：

当 j = 4 时，dp[4] = true 且 s[4:8] = "code" 在字典中，所以 dp[8] = true。
此时直接 break，避免继续检查 j = 5, 6, 7 的情况
*/

