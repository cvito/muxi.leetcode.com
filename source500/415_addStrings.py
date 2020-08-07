class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        integer1, integer2 = 0, 0
        len_num1, len_num2 = len(num1), len(num2)
        for i in range(len_num1):
            integer1 += int(num1[len_num1-i-1])*(10**i)
        for i in range(len_num2):
            integer2 += int(num2[len_num2-i-1])*(10**i)
        return str(integer1+integer2)

s = Solution()
r = s.addStrings("123", "123")
print(r)
