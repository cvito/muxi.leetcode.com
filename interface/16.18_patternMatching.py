class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = sum(1 for ch in pattern if ch == 'a')
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)

        if not value:
            return count_b == 0
        if not pattern:
            return False

        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - count_a * len_a
            ok = (count_b == 0 and rest == 0) or (count_b != 0 and rest % count_b == 0)
            if not ok: continue

            len_b = 0 if count_b == 0 else rest // count_b
            pos, corrent = 0, True
            value_a, value_b = None, None

            for ch in pattern:
                if ch == 'a':
                    sub = value[pos:pos+len_a]
                    if not value_a:
                        value_a = sub
                    elif value_a != sub:
                        corrent = False
                        break
                    pos += len_a
                else:
                    sub  = value[pos:pos+len_b]
                    if not value_b:
                        value_b = sub
                    elif value_b != sub:
                        corrent = False
                        break
                    pos += len_b

            if corrent and value_a != value_b:
                return True
        return False
