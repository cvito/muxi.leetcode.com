
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_visited = {}
        def helper(node: 'Node') -> 'Node':
            if not node: return None
            if node in node_visited:
                return node_visited[node]
            clone_node = Node(node.val, [])
            node_visited[node] = clone_node
            for neigh in node.neighbors:
                clone_node.neighbors.append(helper(neigh))
            return clone_node
        return helper(node)

