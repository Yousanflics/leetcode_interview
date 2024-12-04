#include <iostream>
#include<vector>
#include <unordered_set>
#include<queue>
using namespace std;
struct TreeNode
{
    int val;
    TreeNode* left;
    TreeNode& right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& levelorder) {
        if(inorder.empty() || levelorder.empty()) return nullptr;
        TreeNode* root = new TreeNode(levelorder[0]);
        auto rootPos = find(inorder.begin(), inorder.end(), levelorder[0]);
        int leftSize = distance(inorder.begin(), rootPos);
        vector<int> leftInorder(inorder.begin(), rootPos);
        vector<int> rightInorder(rootPos+1, inorder.end());
        vector<int> leftLevelorder, rightLevelorder;
        unordered_set<int> leftSet(leftInorder.begin(), leftInorder.end());
        for(int val : levelorder) {
            if(leftSet.count(val)) leftLevelorder.push_back(val);
            else if(find(rightInorder.begin(), rightInorder.end(), val) != rightInorder.end()) {
                rightLevelorder.push_back(val);
            }
        }
        root->left = builTree(leftInorder, leftLevelorder);
        root->right = buildTree(rightInorder, rightLevelorder);
        return root;
    }
};

// 测试用例
int main() {
    vector<int> inorder = {9, 3, 15, 20, 7};
    vector<int> levelorder = {3, 9, 20, 15, 7};

    Solution solution;
    TreeNode* root = solution.buildTree(inorder, levelorder);

    // 打印树的前序遍历结果
    function<void(TreeNode*)> preorder = [&](TreeNode* node) {
        if (!node) return;
        cout << node->val << " ";
        preorder(node->left);
        preorder(node->right);
    };

    preorder(root); // 输出: 3 9 20 15 7
    return 0;
}

