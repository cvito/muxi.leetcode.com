class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.previous = None

    def rem_old_node(self):
        self.previous.next = self.next
        self.next.previous = self.previous

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self, key: int) -> int:
        if key in self.cache_dict:
            node = self.cache_dict[key]
            node.rem_old_node()
            self.add_new_node_to_head(node)
            return node.val
        return -1


    def add_new_node_to_head(self, new_node):
        first_node = self.head.next
        self.head.next = new_node
        new_node.previous = self.head
        new_node.next = first_node
        first_node.previous = new_node

    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            node = self.cache_dict[key]
            if node.val == value: return
            node.val = value
            node.rem_old_node()
            self.add_new_node_to_head(node)
            return

        if len(self.cache_dict) >= self.capacity:
            lastest_node = self.tail.previous
            del self.cache_dict[lastest_node.key]
            lastest_node.rem_old_node()
            del lastest_node
        new_node = ListNode(key, value)
        self.add_new_node_to_head(new_node)
        self.cache_dict[key] = new_node
        return



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(1)
obj.put(2, 1)
param_1 = obj.get(2)
obj.put(3, 2)
param_2 = obj.get(2)
param_3 = obj.get(3)