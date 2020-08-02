# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        def helper(node: TreeNode) -> TreeNode:
            left_node = node.left
            right_node = node.right
            if not left_node and not right_node: return node
            if not left_node:
                right_last_node = helper(right_node)
                return right_last_node
            if not right_node:
                left_last_node = helper(left_node)
                node.right = left_node
                node.left = None
                return left_last_node
            left_last_node = helper(left_node)
            right_last_node = helper(right_node)
            left_last_node.right = right_node
            left_last_node.left = None
            node.right = left_node
            node.left = None
            return right_last_node

        helper(root)
        return
