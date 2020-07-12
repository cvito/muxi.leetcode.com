from typing import List

class Trie:
    def __init__(self):
        self.next = {}
        self.isEnd = False
    def insert(self, word):
        curr_node = self
        for i in range(len(word) - 1, -1, -1):
            t = ord(word[i]) - ord('a')
            if t not in curr_node.next:
                curr_node.next[t] = Trie()
            curr_node = curr_node.next[t]
        curr_node.isEnd = True


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        l = len(sentence)
        if not dictionary: return l
        root = Trie()
        for word in dictionary:
            root.insert(word)
        dp = [l] * (l+1)
        dp[0] = 0
        for i in range(1, l+1):
            dp[i] = dp[i-1]+1
            cur_node = root
            for j in range(i, 0, -1):
                t = ord(sentence[j-1]) - ord('a')
                if t not in cur_node.next:
                    break
                elif cur_node.next[t].isEnd:
                    dp[i] = min(dp[i], dp[j-1])

                if dp[i] == 0:
                    break
                cur_node = cur_node.next[t]
        return dp[l]


s = Solution()
r = s.respace(["looked","just","like","her","brother"], "jesslookedjustliketimherbrother")
print(r)




