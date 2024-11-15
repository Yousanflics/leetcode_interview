class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root){
        vector<int> res;
        solve(root, res);
        return res;
    }
    vector<int> solve(TreeNode* root, vector<int>&ans) {
        if(root == nullptr) return ans;
        solve(root->left, ans);
        solve(root->right, ans);
        ans->push_back(root->val);
        return ans;
    }
};
