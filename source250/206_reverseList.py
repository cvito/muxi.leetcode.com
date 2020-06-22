# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

## 递归方法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        def reverse(node: ListNode):
            if not node.next:
                return node
            else:
                new_head = reverse(node.next)
                new_node = node.next
                new_node.next = node
                node.next = None
                return new_head
        return reverse(head)


## 迭代方法
class SolutionV2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        pre_node, node = head, head.next
        pre_node.next = None
        while node is not None:
            next_node = node.next
            if not next_node:
                node.next = pre_node
                return node
            else:
                node.next = pre_node
                pre_node = node
                node = next_node
        return head