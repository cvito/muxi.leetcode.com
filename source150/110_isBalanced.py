# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node: TreeNode) -> (int, bool):
            if not node: return 0, True
            if not node.left and not node.right: return 1, True
            left_depth, ok = helper(node.left)
            print("val: {}, left_depth: {}, ok: {}".format(node.val, left_depth, ok))
            if not ok: return 0, False
            right_depth, ok = helper(node.right)
            print("val: {}, right_depth: {}, ok: {}".format(node.val, right_depth, ok))
            if not ok: return 0, False
            if abs(right_depth - left_depth) > 1:
                return 0, False
            else:
                return max(left_depth, right_depth)+1, True
        _, ok = helper(root)
        return ok

