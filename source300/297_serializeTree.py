# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        def serializeTree(root):
            if root is None:
                res.append('null')
                return
            res.append(root.val)
            serializeTree(root.left)
            serializeTree(root.right)
        serializeTree(root)
        return ",".join('%s' %id for id in res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print(data)
        if not data: return []
        nums = data.split(",")
        def deserializeTree(index):
            if nums[index] == 'null': return index, None
            node = TreeNode(int(nums[index]))
            l, left_node = deserializeTree(index+1)
            node.left = left_node
            r, right_node = deserializeTree(l+1)
            node.right = right_node
            return r, node
        return deserializeTree(0)[1]





# Your Codec object will be instantiated and called as such:
codec = Codec()
codec.deserialize(codec.serialize(TreeNode(1)))