from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        seg_size = 4
        res = list()
        segments = [0] * seg_size
        def helper(seg_id, seg_start):
            if seg_id == seg_size:
                if seg_start == len(s):
                    ip_addr = '.'.join(str(seg) for seg in segments)
                    res.append(ip_addr)
                return

            if seg_start == len(s):
                return

            if s[seg_start] == '0':
                segments[seg_id] = 0
                helper(seg_id+1, seg_start+1)

            addr = 0
            for segEnd in range(seg_start, len(s)):
                addr = addr * 10 + (ord(s[segEnd])-ord('0'))
                if 0 < addr <= 0xff:
                    segments[seg_id] = addr
                    helper(seg_id+1, segEnd+1)
                else:
                    break
        helper(0, 0)
        return res
