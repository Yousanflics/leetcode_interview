/*
算是二叉树层序遍历的一个变题，核心是需要一个额外的 queue
*/
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> res
        queue<ListNode*> q = {{root}};
        while(!q.empty()) {
            int n = q.size();
            for(int i = n; i > 0; --i){
                int sum;
                ListNode* t = q.front(); q.pop();
                sum += t->val;
                if(t->left) q.push(t->left);
                if(t->right) q.push(t->right);
            }
            res.push_back(sum/n);
        }
        return res;
    }
};
