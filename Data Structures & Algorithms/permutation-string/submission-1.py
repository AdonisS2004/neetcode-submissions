class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # helper function
        def c2i(c):
            """ for indexing """
            return ord(c)-ord('a')
        
        s1_len, s2_len = len(s1), len(s2)

        # length check
        if s1_len > s2_len:
            return False

        # create hashing
        perm_hash = [0]*26
        for c in s1:
            perm_hash[c2i(c)] += 1
        
        # construct fixed sized window
        window_hash = [0]*26
        l,r = 0, 0
        while r < s1_len:
            c = s2[r]
            window_hash[c2i(c)] += 1
            r += 1
         # find hash

        while r < s2_len:
            if window_hash == perm_hash:
                return True
            c = s2[l]
            window_hash[c2i(c)] -= 1
            l += 1
            c = s2[r]
            window_hash[c2i(c)] += 1
            r += 1
        
        if window_hash == perm_hash:
            return True
        return False