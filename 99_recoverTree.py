# Definition for a binary tree node.
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        priority_queue = []
        heapq.heapify(priority_queue)

        while not heapq.heappop(priority_queue) or not root
