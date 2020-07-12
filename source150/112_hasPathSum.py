# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def helper(node, path_sum) -> bool:
            if not node: return False
            if not node.left and not node.right:
                #叶子节点
                return path_sum + node.val == sum

            return helper(node.left, path_sum+node.val) or helper(node.right, path_sum+node.val)
        return helper(root, root.val)