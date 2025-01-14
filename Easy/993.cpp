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
题目分析：
- 这道题定义了一种二叉树数的表兄弟结点，不属于同一个父结点，但是深度相同，现在给了两个结点值，问它们代表的结点是否是表兄弟结点。由于表兄弟结点一定是属于同一层的，所以可以使用二叉树的层序遍历，就像之前那道 Binary Tree Level Order Traversal

代码分析：
- 为什么判断 isX 和 isY 是 cur->val 去判断 ==，而return false 的时候用确实 cur->left->val 和 cur->right->val

总结：
- 这道题本质上还是考察二叉树的**层序遍历**或者也可以理解为层序遍历的 fellow up，所以属于 Easy 水平并且需要做到熟知必会
*/
class Solution {
public:
    bool isCousins(TreeNode* root, int x, int y) {
        queue<TreeNode*> q{{root}};
        // 标记位是需要的因为如果没有标记位这两个不知道后面有没有找到，不管是找到了一个还是两个，都需要在遍历的时候进行标记
        bool isX = false, isY = false;
        while(!q.empty()) {
            for(int i = q.size(), i > 0; i--) {
                // 从队列首部获取元素然后知道 x 和 y
                TreeNode* cur = q.front(), q.pop();
                if(cur->val == x) isX = true;
                if(cur->val == y) isY = true;
                // 在层序遍历的过程中设置条件判断，如果cur的左右存在且等于 x 和 y那就包不是 cousin 直接 return
                // 这里需要注意的是 x 和 y 跟 left 和 right 可能是反着的所以会有两种情况都需要考虑到
                if(cur->left && cur->right) {
                    int left = cur->left->val, right = cur->right->val;
                    if((left == x && right == y || left == y && right == y)) return false;
                }
                if(cur->left) q.push(cur->left);
                if(cur->right) q.push(cur->right);
            }
            if(isX && isY) return true;
            if(isX || isY) return false;
        }
        return false;
    }
};
