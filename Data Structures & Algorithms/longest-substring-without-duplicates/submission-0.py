class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l,r, n = 0,0, len(s)
        sublen = 0
        max_sublen = 0
        while r < n:
            while s[r] in unique:
                unique.remove(s[l])
                sublen -= 1
                l += 1
            unique.add(s[r])
            sublen += 1
            max_sublen = max(max_sublen, sublen)
            r += 1
        return max_sublen