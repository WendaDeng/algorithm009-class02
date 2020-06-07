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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n = inorder.size();
        for (int i = 0; i < n; i++)
            index[inorder[i]] = i;

        return buildTree(preorder, 0, n - 1, inorder, 0, n - 1);
    }
private:
    unordered_map<int, int> index;
    TreeNode* buildTree(vector<int>& preorder, int pLeft, int pRight, vector<int>& inorder, int iLeft, int iRight) {
        if (pLeft > pRight) return NULL;

        // process current level logic
        TreeNode *root = new TreeNode(preorder[pLeft]);
        int idx = index[preorder[pLeft]];
        int left_tree_size = idx - iLeft;

        // drill down
        root->left = buildTree(preorder, pLeft+1, pLeft+left_tree_size, inorder, iLeft, idx-1);
        root->right = buildTree(preorder, pLeft+left_tree_size+1, pRight, inorder, idx+1, iRight);

        return root;
    }
};
