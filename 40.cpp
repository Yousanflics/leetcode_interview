/*
39 的升级版，找到数组中和为 target 的元素且每个元素的使用不可以重复
跟 39 的实现比多了排序，为什么需要排序？重复的元素会相邻，可以轻松地跳过重复的元素避免生成
重复的组合
- [1, 1, 2]
通过对比 candidates[i] == candidates[i - 1] 跳过
同时剪枝优化：递归过程中，如果 target < 当前的候选数（index[cur]）可以直接停止当前分支的
搜索，减少不必要的计算
*/
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> cur;
        // 需要排序
        sort(candidates.begin(), candidates.end());
        // 构造所有可能出现的组合
        dfs(candidates, target, 0, cur, res);
        return res;
    }
    void dfs(vector<int>& candidates, int target, int start, vector<int>& cur, vector<vector<int>>& res) {
        // 跟 39 一样
        if (target < 0) return;
        if (target == 0) { res.push_back(cur); return; }
        // 跟 39 不一样的是对 candidates[i] 和 candidates[i-1]进行减枝
        for (int i = start; i < candidates.size(); ++i) {
            // 只在同一层递归中生效即去重，如果两个相邻直接 continue 跳过
            if (i > start && candidates[i] == candidates[i - 1]) continue;
            // 把当前遍历的结果放进 cur 中记录起来
            cur.push_back(candidates[i]);
            // 跟 39 same
            dfs(candidates, target - candidates[i], i + 1, cur, res);
            // 回溯到最开始的起始状态方便后面的 push_back
            cur.pop_back();
        }
    }
};
