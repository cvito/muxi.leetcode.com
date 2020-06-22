from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
         res_list = []
         def helper(left, right, res_str):
             if left == 0 and right == 0:
                 res_list.append(res_str)
                 return
             if left > 0:
                 res_str += '('
                 helper(left-1, right, res_str)
                 res_str = res_str[:-1]
             if right > left:
                 res_str += ')'
                 helper(left, right-1, res_str)
             return
         helper(n, n, "")
         return res_list


s = Solution()
res = s.generateParenthesis(3)
print(res)


