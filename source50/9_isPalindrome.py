
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。

"""
#思路
1. 个位不能为0
2. 最高位不能是符号
3. 得是一个整数
"""


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    else:
        y = str(x)[::-1]
        print(y)
        if y == str(x):
            return True
        else:
            return False





