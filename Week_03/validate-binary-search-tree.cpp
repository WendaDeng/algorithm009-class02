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
    bool isValidBST(TreeNode* root) {
        if (!root) return true;
        // 根据中序遍历的结果判断
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
};
