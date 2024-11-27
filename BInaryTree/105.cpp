/*
二叉树 前序和中序遍历重建这棵树
中序： 左 根 右
前序： 根 左 右
前/后 + 中 = 唯一确定一颗二叉树
前 + 后 无法唯一确定一颗二叉树
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
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        return buildTree(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }
    TreeNode *buildTree(vector<int> &preorder, int pLeft, int pRight, vector<int> &inorder, int iLeft, int iRight) {
        if (pLeft > pRight || iLeft > iRight) return NULL;
        int i = 0;
        for (i = iLeft; i <= iRight; ++i) {
            if (preorder[pLeft] == inorder[i]) break;
        }
        TreeNode *cur = new TreeNode(preorder[pLeft]);
        cur->left = buildTree(preorder, pLeft + 1, pLeft + i - iLeft, inorder, iLeft, i - 1);
        cur->right = buildTree(preorder, pLeft + i - iLeft + 1, pRight, inorder, i + 1, iRight);
        return cur;
    }
};

/*
前序，前序首先遍历的肯定是根->原二叉树根节点就知道了
树中没有相同的元素->可以通过确定中序中根的位置，可以得到左右两个部分，继续递归调用

前序遍历（preorder）：[3, 9, 20, 15, 7]
中序遍历（inorder）：[9, 3, 15, 20, 7]

得到 root = 3 中序中的 i = 1
中序中 9 0-0 是左子树 2-4 是右子树
i - iLeft 是 中序 中从 root 到起始的位置, inorder的位置变成了 iLeft 到 i - 1(因为要取=)
递归调用 cur-left = bt(pre, pLeft + 1, pLeft + i - iLeft, inorder, iLeft, i - 1)
*/
