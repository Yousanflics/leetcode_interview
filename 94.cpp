// 常见的递归的解决方式
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorder(root, res);
        return res;
    }
private:
    void inorder(TreeNode* node, vector<int> res) {
        if(!node) return;
        inorder(node->left, res);
        res.push_back(node->val);
        inorder(node->right);
    }
};

// 一般考察迭代的实现 辅助 stack<TreeNode*>
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> st;
        TreeNode* curr = root;
        while(curr || !st.empty()){
            while(curr) {
                st.push(curr);
                curr = curr->left;
            }
            curr = st.top();
            st.pop();
            result.push_back(curr->val);
            curr = curr->right;
        }
        return res;
    }
};
