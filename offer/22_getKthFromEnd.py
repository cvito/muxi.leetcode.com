# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        first_node, last_node = head, head
        dist = 1
        while last_node:
            if not last_node.next: break
            last_node = last_node.next
            if dist >= k:
                first_node = first_node.next
            else:
                dist += 1
        return first_node
