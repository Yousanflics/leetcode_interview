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

/*
 树的广度优先遍历 BFS 优先考虑使用 queue，queue.front(）获取队头元素 queue.back(). queue.push() queue.pop
*/
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(!root) return {};
        vector<vector<int>> res;
        queue<ListNode*> q {{root}};
        while(!q.empty()) {
            vector<int> oneLevel;
            for(int i = q.size(), i > 0; --i){
                ListNode* node = q.front(); q.pop();
                oneLevel.push_back(node->val);
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
            }
            res.push_back(oneLevel);
        }
        return res;
    }
};
