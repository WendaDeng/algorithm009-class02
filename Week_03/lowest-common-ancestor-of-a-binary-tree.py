# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 虽然很 fancy ，但是运行时间会增加 6 倍！
        if root in (None, p, q): return root

        left, right = (self.lowestCommonAncestor(kid, p, q)
                for kid in (root.left, root.right))

        return root if left and right else left or right

