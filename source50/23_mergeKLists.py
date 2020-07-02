# Definition for singly-linked list.
import heapq
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val < other.val

class MyListNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        if not self.node: return True
        if not other.node: return False
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        hp = [MyListNode(node) for node in lists]
        heapq.heapify(hp)
        head = ListNode(0)
        path = head
        while len(hp) != 0:
            myNode = heapq.heappop(hp)
            if not myNode.node: continue
            path.next = myNode.node
            path = path.next
            if myNode.node.next:
                heapq.heappush(hp, MyListNode(myNode.node.next))
        return head.next


