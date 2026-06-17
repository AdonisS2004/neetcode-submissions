class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen, tlen = len(s), len(t)
        if tlen > slen:
            return ""
        
        l,r = 0,0
        small_l, small_r = -1, -1
        
        unique_t = {}
        m = 0
        for c in t:
            if c not in unique_t:
                unique_t[c] = 0
                m += 1
            unique_t[c] += 1
    
        found_map = dict()
        found_count = 0

        # find indices
        while r < slen:
            # print(f"BEFORE R UPDATE")
            # print(f"{slen=}; {tlen=}; (l,r)=({l},{r}); (small_l,small_r)=({small_l},{small_r});") 
            # print(f"{m=}, {found_count=}, {unique_t=}, {found_map=}, {s[l:r]}")
            rc = s[r]
            if rc in unique_t:
                if rc not in found_map:
                    found_map[rc] = 0
                found_map[rc] += 1
                if found_map[rc] == unique_t[rc] and found_map[rc]-1 < unique_t[rc]:
                    found_count += 1
            r += 1
            # print(f"AFTER R UPDATE")
            # print(f"{slen=}; {tlen=}; (l,r)=({l},{r}); (small_l,small_r)=({small_l},{small_r});") 
            # print(f"{m=}, {found_count=}, {unique_t=}, {found_map=}, {s[l:r]}")
            # move l to the left when substring is found
            while l < r and found_count == m:
                # print(f"SUBSTRING FOUND, UPDATING L")
                # print(f"{slen=}; {tlen=}; (l,r)=({l},{r}); (small_l,small_r)=({small_l},{small_r});") 
                # print(f"{m=}, {found_count=}, {unique_t=}, {found_map=}, {s[l:r]}")
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

        

