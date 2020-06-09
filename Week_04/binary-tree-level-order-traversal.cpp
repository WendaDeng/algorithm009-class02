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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root)  return res;
        // 使用两个 vector 分别保存当前层和下一层的节点
        vector<TreeNode *> cur, next;
        // 保存当前层的数据
        vector<int> vals;

        cur.push_back(root);
        while (!cur.empty() || !next.empty()) {
            // 遍历当前层节点
            for (int i = 0; i < cur.size(); i++) {
                TreeNode *node = cur[i];
                vals.push_back(node->val);
                if (node->left) next.push_back(node->left);
                if (node->right) next.push_back(node->right);
            }
            // 先清空当前层节点，同时指向下一层节点，最后下一层节点清空
            cur.clear();
            cur = next;
            next.clear();
            // 将当前层的数据保存，然后清空vector
            res.push_back(vals);
            vals.clear();
        }
        return res;
    }
};
