class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen, tlen = len(s), len(t)

        # base case: length check
        if tlen > slen:
            return ""
        
        l,r = 0,0
        # used to keep track of the indices for smallest substring
        small_l, small_r = -1, -1
        

        # construct map for unique t chars are frequencies
        unique_t = {}
        m = 0
        for c in t:
            if c not in unique_t:
                unique_t[c] = 0
                m += 1
            unique_t[c] += 1
    
        # elements found during search
        found_map = {}
        found_count = 0

        # sliding window search
        while r < slen:
            rc = s[r]
            if rc in unique_t:
                if rc not in found_map:
                    found_map[rc] = 0
                found_map[rc] += 1
                if found_map[rc] == unique_t[rc] and found_map[rc]-1 < unique_t[rc]:
                    found_count += 1
            r += 1
            # move l to the left when substring is found
            while l < r and found_count == m:
                # update small_l and small_r
                if small_l == -1 and small_r == -1:
                    small_l, small_r = l, r
                else:
                    curr_dist = r-l
                    prev_dist = small_r-small_l
                    if curr_dist < prev_dist:
                        small_l, small_r = l, r
                # update l
                lc = s[l]
                if lc in unique_t:
                    found_map[lc] -= 1
                    if found_map[lc] < unique_t[lc]:
                        found_count -= 1
                l += 1
        
        # construct result
        res = ""
        if small_l == -1 and small_r == -1:
            return res
        while small_l < small_r:
            res += s[small_l]
            small_l += 1
        return res

        

