# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        vals = []
        cur_level_vals = []
        cur_level_nodes = [root]
        next_level_nodes = []
        while True:
            while cur_level_nodes:
                node = cur_level_nodes.pop(0)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
                cur_level_vals.append(node.val)
            vals.append(cur_level_vals)
            cur_level_vals = []
            if next_level_nodes:
                cur_level_nodes = next_level_nodes
                next_level_nodes = []
            else:
                break
        return vals
