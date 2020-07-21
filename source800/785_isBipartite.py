from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph: return True
        dict = {}
        for i in range(len(graph)):
            for j in graph[i]:
                if i not in dict and j not in dict:
                    dict[i] = 1
                    dict[j] = 2
                    continue
                if i in dict and j in dict:
                    if dict[i] == dict[j]:
                        return False
                    else:
                        continue
                if i not in dict:
                    dict[i] = 2 if dict[j] == 1 else 1
                    continue
                if j not in dict:
                    dict[j] = 2 if dict[i] == 1 else 1
                    continue
        return True

s = Solution()
r = s.isBipartite([[3],[2,4],[1],[0,4],[1,3]])
print(r)

