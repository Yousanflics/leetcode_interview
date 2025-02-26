/*
要求出所有结果的集合这种 case 一般都需要用到 DFS 调用递归来解决
题目的意思是求 1 - n 这 n 个数字力 k 个数的组合 1，2 和 2，1 是一个意思
1.建立一个保存最终结果的 res 大集合，定义一个保存每一个组合的小集合 cur，每一次保存一个数 tmp 到 cur 中，如果 cur 的数字到 k 个把cur保存到最终结果，否则下一层中继续调用递归


Q：为什么 for loop 中需要 cur.pop_back() 因为递归的时候需要回溯，回溯到之前的状态放下一个状态的数据加入进来

递归与回溯的流程：

当选择当前数字 i 加入组合（cur.push_back(i)），并递归进入下一层时，会生成以 i 开头的所有有效组合。

递归返回后，说明以 i 开头的所有情况已经处理完毕。此时需要将 i 从组合中移除（cur.pop_back()），以便后续循环尝试下一个数字（如 i+1）。

*/
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> cur;
        dfs(n, k, 1, cur, res);
        return res;
    }
    // level 表示从哪个数字开始，也可以叫做 startflag 吧
    void dfs(int n, in k, int level, vector<int>& cur, vector<vector<int>>& res) {
        // 这里里面已经限制了 cur.size() 只能有 k 个数字大小
        if(cur.size() == k) {
            res.push_back(cur);
            return;
        }
        for(int i = level; i <= n; ++i) {
            cur.push_back(i);
            dfs(n, k, i + 1, cur, res);
            cur.pop_back();
        }
    }
};
