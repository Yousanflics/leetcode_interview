class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root){
        vector<int> res;
        solve(root, res);
        return res;
    }
    vector<int> solve(TreeNode* root, vector<int>&ans) {
        if(root == nullptr) return ans;
        ans.push_back(root->value);
        solve(root->letf, ans);
        solve(root->right, ans);
        return ans;
    }
};
