class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = [0]*26
        t_hash = [0]*26
        for c in s:
            s_hash[ord(c)-ord('a')] += 1
        for c in t:
            t_hash[ord(c)-ord('a')] += 1
        return s_hash == t_hash