/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) return {};
        vector<vector<int>> res;
        queue<TreeNode*> q{{root}};
        // 标记位，奇数位置需要翻转，从 0 开始，第一个是从左到右
        bool leftToRight = true;
        while (!q.empty()) {
            // 通过赋值就不会导致 q.size() 的变化而影响到 i 的遍历区间了
            int size = q.size();
            vector<int> oneLevel(size);
            for (int i = 0; i < size; ++i) {
                TreeNode *t = q.front(); q.pop();
                // 如果需要反向输出则 idx = size - 1 - i;
                int idx = leftToRight ? i : (size - 1 - i);
                oneLevel[idx] = t->val;
                if (t->left) q.push(t->left);
                if (t->right) q.push(t->right);
            }
            // 每输出一行自动取反一次
            leftToRight = !leftToRight;
            res.push_back(oneLevel);
        }
        return res;
    }
};
