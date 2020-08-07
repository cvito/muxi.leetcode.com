# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node: TreeNode) -> (int, int):
            if not node: return 0, 0
            left_node = node.left
            right_node = node.right
            if not left_node and not right_node: return node.val, 0
            left_include_val, left_exclude_val = helper(left_node)
            right_include_val, right_exclude_val = helper(right_node)
            include_val = left_include_val + right_include_val
            exclude_val = left_exclude_val + right_exclude_val
            return node.val+exclude_val, max(include_val, exclude_val, left_include_val+right_exclude_val, left_exclude_val+right_include_val)
        return max(helper(root))


