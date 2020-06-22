# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return 0

        def maxPath(node):
            cur_max, max_sum = node.val, node.val
            if not node.left and not node.right: return cur_max, max_sum
            if not node.right and node.left is not None:
                left_max, left_max_sum = maxPath(node.left)
                cur_max = max(cur_max, left_max + node.val)
                max_sum = max(max_sum, left_max_sum, left_max + node.val)
            elif not node.left and node.right is not None:
                right_max, right_max_sum = maxPath(node.right)
                cur_max = max(cur_max, right_max + node.val)
                max_sum = max(max_sum, right_max_sum, right_max + node.val)
            else:
                left_max, left_max_sum = maxPath(node.left)
                right_max, right_max_sum = maxPath(node.right)
                cur_max = max(cur_max, left_max + node.val, right_max + node.val)
                max_sum = max(max_sum, left_max_sum, right_max_sum)
                max_sum = max(max_sum, left_max + node.val, right_max + node.val)
                max_sum = max(max_sum, left_max + right_max + node.val)
            return cur_max, max_sum

        _, res = maxPath(root)
        return res


class Solution_V2:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node: return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain

            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)

            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum

