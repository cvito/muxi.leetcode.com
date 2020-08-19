# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head: return []
        if not head.next: return [head.val]
        return self.reversePrint(head.next).append(head.val)

