from typing import List
import collections

# 超时
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j: continue
                new_str = words[i] + words[j]
                if new_str[::-1] == new_str: res.append([i, j])
        return res

class Solution_V2:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        char_dict = collections.defaultdict(list)
        for i in range(len(words)):
            key = words[i][-1] if words[i] else ""
            char_dict[key].append(i)
        res = []
        for i in range(len(words)):
            word = words[i]
            if word:
                for j in char_dict[word[0]]:
                    if i == j: continue
                    new_str = words[i] + words[j]
                    if new_str[::-1] == new_str: res.append([i, j])
                for k in char_dict[""]:
                    if words[i][::-1] ==  words[i]: res.append([i, k])
            else:
                l = i-1
                while l >= 0:
                    new_str = words[l]
                    if new_str and new_str[::-1] == new_str: res.append([i, l])
                    l -= 1
                h = i+1
                while h < len(words):
                    new_str = words[l]
                    if not new_str: res.append([i, h])
                    elif new_str[::-1] == new_str: res.append([i, h])
                    h += 1
        return res


s = Solution_V2()
#r = s.palindromePairs(["abcd","dcba","lls","s","sssll"])
#r = s.palindromePairs(["bat","tab","cat"])
#r = s.palindromePairs(["a",""])
r = s.palindromePairs(["a","abc","aba","",""])
print(r)


