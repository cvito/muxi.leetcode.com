# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S: return None
        pos, node_list = 0, list()
        while pos <= len(S)-1:
            level = 0
            while S[pos] == '-':
                level += 1
                pos += 1
            num = 0
            while pos < len(S) and S[pos].isdigit():
                num = num * 10 + int(S[pos])
                pos += 1
            node = TreeNode(num)
            if level == len(node_list):
                if node_list: node_list[-1].left = node
            else:
                node_list = node_list[:level]
                node_list[-1].right = node
            node_list.append(node)
        return node_list[0]

s = Solution()
s.recoverFromPreorder("1-2--3--4-5--6--7")