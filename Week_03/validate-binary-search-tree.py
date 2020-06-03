# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:   return True

        pre = None
        nodes = []
        while root or len(nodes):
            while root:
                nodes.append(root)
                root = root.left
            root = nodes.pop()
            if pre and pre.val >= root.val:  return False
            pre = root
            root = root.right
        return True
