/*
要求出所有结果的集合这种 case 一般都需要用到 DFS 调用递归来解决
题目的意思是求 1 - n 这 n 个数字力 k 个数的组合 1，2 和 2，1 是一个意思
1.建立一个保存最终结果的 res 大集合，定义一个保存每一个组合的小集合 cur，每一次保存一个数 tmp 到 cur 中，如果 cur 的数字到 k 个把cur保存到最终结果，否则下一层中继续调用递归


Q：为什么 for loop 中需要 cur.pop_back() 因为递归的时候需要回溯，回溯到之前的状态放下一个状态的数据加入进来

递归与回溯的流程：

当选择当前数字 i 加入组合（cur.push_back(i)），并递归进入下一层时，会生成以 i 开头的所有有效组合。

递归返回后，说明以 i 开头的所有情况已经处理完毕。此时需要将 i 从组合中移除（cur.pop_back()），以便后续循环尝试下一个数字（如 i+1）。


方法 2：



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
    // solution II
    /*
    思路如下: 
    其实这个题目还有一个数学解决方法，排列组合的逻辑
    C(n, k) = C(n-1, k-1) + C(n-1, k)
    例如：
    C(4, 2) = C(3, 1) + C(3, 2)
    展开说说：C(3, 1) 的所有情况：[1], [2], [3]，还有 C(3, 2) 的所有情况：[1, 2], [1, 3], [2, 3]。可以发现二者加起来为6，正好是 C(4, 2) 的总数。仔细查看，C(3, 2)的所有情况包含在 C(4, 2) 之中，但是 C(3, 1) 的每种情况只有一个数字，而需要是 k=2 位，针对这种可以每一个都加上最后4，于是变成了：[1, 4], [2, 4], [3, 4]，加上 C(3, 2) 的所有情况：[1, 2], [1, 3], [2, 3]，正好就得到了 n=4, k=2 的所有情况了，具体代码实现如下：


    cons: 耗时太长了
    */
    vector<vector<int>> combine(int n, int k) {
        //两个if是递归的终止条件
        if(k > n || k < 0) return {};
        if(k == 0) return {{}};
        vector<vector<int>> res = combine(n - 1, k - 1);
        //第一个循环的 &a：用于直接修改原数据，保证组合的正确生成。
        for(auto &a : res) a.push_back(n);
        //第二个循环的 &a：用于避免拷贝临时对象的元素，提升性能
        for(auto &a : combine(n - 1, k)) res.push_back(a);
        return res;
    }
};
