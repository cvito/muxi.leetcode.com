class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"

        def addStrings(num_str1: str, num_str2: str) -> str:
            str1_len, str2_len = len(num_str1)-1, len(num_str2)-1
            add = 0
            res = list()
            while str1_len >= 0 or str2_len >= 0 or add != 0:
                val1 = int(num_str1[str1_len]) if str1_len >= 0 else 0
                val2 = int(num_str2[str2_len]) if str2_len >= 0 else 0
                result = val1 + val2 + add
                res.append(str(result % 10))
                add = result // 10
                str1_len -= 1
                str2_len -= 1
            return "".join(res[::-1])

        ans = "0"
        num1_len, num2_len = len(num1), len(num2)
        for i in range(num2_len-1, -1, -1):
            add = 0
            val2 = int(num2[i])
            curr = ["0"] * (num2_len - i - 1)
            for j in range(num1_len-1, -1, -1):
                result = int(num1[j]) * val2 + add
                curr.append(str(result % 10))
                add = result // 10
            if add > 0:
                curr.append(str(add))
            curr = "".join(curr[::-1])
            ans = addStrings(ans, curr)
        return ans


class Solution_V2:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        ansArr = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                ansArr[i + j + 1] += x * int(num2[j])

        for i in range(m + n - 1, 0, -1):
            ansArr[i - 1] += ansArr[i] // 10
            ansArr[i] %= 10

        index = 1 if ansArr[0] == 0 else 0
        ans = "".join(str(x) for x in ansArr[index:])
        return ans


s = Solution_V2()
r = s.multiply("1024", "6")
print(r)
