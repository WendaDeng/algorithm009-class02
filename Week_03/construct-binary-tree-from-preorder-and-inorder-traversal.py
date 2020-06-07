# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) != len(inorder) or len(preorder) == 0: return None

        idx = inorder.index(preorder[0])

        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:idx+1], inorder[0:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root
