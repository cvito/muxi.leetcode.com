# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n: return []
        def helper(start, end):
            if start > end:
                return [None]
            all_tree = []
            for i in range(start, end+1):
                left_tree = helper(start, i-1)
                right_tree = helper(i+1, end)

                for l in left_tree:
                    for r in right_tree:
                        all_tree.append(TreeNode(i, l, r))
            return all_tree
        return helper(1, n)
