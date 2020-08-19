# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        val_list = list()
        while head:
            val_list.append(head.val)
            head = head.next

        def helper(left: int, right: int, node: TreeNode):
            mid = (left + right + 1) // 2
            node.val = val_list[mid]
            if left <= mid - 1:
                node.left = TreeNode()
                helper(left, mid - 1, node.left)
            if mid + 1 <= right:
                node.right = TreeNode()
                helper(mid + 1, right, node.right)
            return

        root = TreeNode()
        helper(0, len(val_list) - 1, root)
        return root


class Solution_V2:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getLength(head: ListNode) -> int:
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret

        def buildTree(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = (left + right + 1) // 2
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(mid + 1, right)
            return root

        length = getLength(head)
        return buildTree(0, length - 1)

