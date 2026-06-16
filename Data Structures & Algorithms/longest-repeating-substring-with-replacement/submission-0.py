class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique_s = list(set(s)) # constant bounded size since theres at most 26 capital letters --> O(n)
        max_rep = 0
        n = len(s)
        for char in unique_s:
            l,r = 0,0
            sublen = 0
            swaps = k
            while r < n:
                if s[r] == char:
                    r += 1
                    sublen += 1
                    max_rep = max(sublen, max_rep)
                else:
                    while swaps == 0:
                        if s[l] != char:
                            swaps += 1
                        l += 1
                        sublen -= 1
                        max_rep = max(sublen, max_rep)
                    r += 1
                    sublen += 1
                    max_rep = max(sublen, max_rep)
                    swaps -= 1
        return max_rep
