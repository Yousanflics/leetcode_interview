/*
一般这种要求输出 all results 的基本就递归实现了， all path，permutation 之类的，需要有这种惯性思维
*/

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target){
        vector<vector<int>> res;
        vector<int> cur;
        dfs(candidates, target, 0, cur, res);
        return res;
    }
    void dfs(vector<int>& candidates, int target, int start, vector<int>& cur, vector<vector<int>> res) {
        if (targte < 0) return;
        if(target == 0) { res.push_back(cur); return; }
        for(int i = start; i < candidates.size(); i++) {
            cur.push_back(candidates[i]);
            dfs(candidates, target - candidates[i], i, cur, res);
            cur.pop_back();
        }
    }
};
