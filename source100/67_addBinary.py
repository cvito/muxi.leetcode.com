class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a
        res = ""
        carry = 0
        i, j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                val = (carry + int(a[i]) + int(b[j]))
                bit = 0 if val % 2 == 0 else 1
                res = str(bit) + res
                carry = 1 if val >= 2 else 0
                i -= 1
                j -= 1
                continue
            if carry == 1:
                val = carry + int(b[j])
                bit = 0 if val % 2 == 0 else 1
                res = str(bit) + res
                carry = 1 if val >= 2 else 0
                j -= 1
            else:
                break

        if j >= 0:
            res = b[:j+1] + res
        elif carry == 1:
            res = "1" + res
        return res

s = Solution()

# res = s.addBinary("1010", "1011")
rsp = s.addBinary("1", "1101")
print(rsp)
