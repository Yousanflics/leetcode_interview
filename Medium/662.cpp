/*
题目分析：
最近面试和 oa 中经常遇到的一面题，算是 Easy 中比较难的和 Medium 中比较好上手的题目，最近二叉树的题目在面试中大量的遇到，需要中间加强对二叉树的深度广度遍历，层序，zigzag等遍历思路和技巧的学习和理解
*/

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
    int widthOfBinaryTree(TreeNode* root) {
        if(!root) return 0;
        int maxWidth = 0;
        // 添加节点和索引，看 oj 数据类型用 unsigned ll 是最合适的
        queue<pair<TreeNode*, unsigned long long>> q;
        q.push({root, 1});
        while(!q.empty()) {
            int size = q.size();
            unsigned long long left= q.front().second;
            unsigned long long right = q.back().second;
            maxwidth = max(maxWidth, int(right - left + 1));

            for(int i = 0; i < size; i++) {
                auto [node, idx] = q.front();
                q.pop();
                if(node->left) q.push({node->left, idx * 2});
                if(node->right) q.push({node->right, idx * 2 +1});
            }
        }
        return maxWidth;
    }
};

