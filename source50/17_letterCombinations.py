from typing import List


class Solution:
    def __init__(self):
        self.alph_dict = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        def helper(num):
            if not res:
                for val in self.alph_dict[num]:
                    res.append(val)
            else:
                len_tmp = len(res)
                for path in res[:len_tmp]:
                    for val in self.alph_dict[num]:
                        res.append(path + val)
                del res[:len_tmp]

        res = []
        for v in digits: helper(v)
        return res


class Solution_V2:
    def __init__(self):
        self.alph_dict = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return None
        def helper(depth, path):
            if depth == len(digits):
                res.append(path)
                return
            for alph in self.alph_dict[digits[depth]]:
                helper(depth+1, path+alph)
            return

        res = []
        helper(0, "")
        return res



s = Solution_V2()
rsp = s.letterCombinations("22")
print(rsp)