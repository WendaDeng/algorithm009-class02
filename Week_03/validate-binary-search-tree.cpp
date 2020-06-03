/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // 迭代解法，自己维护一个栈，通过中序遍历结果进行判断
    bool isValidBST(TreeNode* root) {
        if (!root) return true;

        TreeNode *pre = NULL;
        stack<TreeNode*> nodes;
        while (root || !nodes.empty()) {
            while (root) {
                nodes.push(root);
                root = root->left;
            }
            root = nodes.top();
            nodes.pop();
            if (pre != NULL && pre->val >= root->val) return false;
            pre = root;
            root = root->right;
        }
        return true;
    }

    // 递归解法
    // bool isValidBST(TreeNode* root) {
    //     return helper(root, LONG_MIN, LONG_MAX);
    // }

    // bool helper(TreeNode* root, long long lower, long long upper) {
    //     if (root == NULL)   return true;
    //     if (root->val <= lower || root->val >= upper)   return false;
    //     return helper(root->left, lower, root->val) &&
    //             helper(root->right, root->val, upper);

    // }
};
