from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while i <= j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i+=1
            j-=1


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        size_a = len(A)
        self.move(size_a, A, B, C)

    def move(self, n, A: List[int], B: List[int], C: List[int]):
        if n == 0: return
        if n == 1:
            C.append(A.pop())
            return
        else:
            self.move(n-1, A, C, B)
            C.append(A.pop())
            self.move(n-1, B, A, C)



