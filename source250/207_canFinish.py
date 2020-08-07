from typing import List

import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        valid = True
        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(node: int):
            nonlocal valid
            visited[node] = 1
            for v in edges[node]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid: return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[node] = 2
            return

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        return valid

