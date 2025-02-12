/*
二叉树列索引常用于 `二叉树的垂序遍历` 相关问题中，它用于标识二叉树节点在 垂直方向上的相对位置，即节点相对根节点的偏移量

假设二叉树的根节点位于列索引 0：
- 向左子树移动时，列索引减1（column = parent_column - 1)
- 向右子树移动时，列索引加1（column = parent_column + 1）

*/

/*
解题思路：
- DFS or BFS 遍历二叉树，记录每个节点的（列索引，行索引，节点值）
- 使用哈希表 map<int, vector<pair<int, int>>>：
    - 键（int）：列索引
    - 值（vector<pair<int, int>>: 储存（行索引，节点值）
-对每个列进行排序：
    - 先按照航索引排序
    - 行索引相同的时候按节点值排序

*/

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x): val(x), left(NULL), right(NULL) {}
}

class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        colMap.clear();
        dfs(root, 0, 0);

        vector<vector<int>> res;

        for(auto &[col, nodes] : colMap) {
            sort(nodes.begin(), nodes.end());

            vector<int> colValues;
            for(auto &[row, val] : nodes) {
                colValues.push_back(val);
            }
            res.push_back(colValues);
        }

        return res;
    }

    void dfs(TreeNode* root, int row, int col) {
        if(!root) return;
        colMap[col].emplace_back(row, root->val);
        dfs(root->left, row + 1, col - 1);
        dfs(root->right, row + 1, col + 1);
    }

private:
    map<int, vector<pair<int, int>>> colMap;
};
