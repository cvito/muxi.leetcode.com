# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def helper(pnode, qnode) -> bool:
            if not pnode and not qnode: return True
            if not pnode and qnode: return False
            if pnode and not qnode: return False
            if pnode.val != qnode.val: return False
            left = helper(pnode.left, qnode.left)
            if not left: return False
            return helper(pnode.right, qnode.right)
        return helper(p, q)