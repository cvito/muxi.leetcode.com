class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2, len_s3  = len(s1), len(s2), len(s3)
        if len_s1 + len_s2 != len_s3:
            return False
        
