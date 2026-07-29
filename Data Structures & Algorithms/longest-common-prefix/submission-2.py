class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        res = []
        ref = strs[0]
        m = min([len(s) for s in strs])
        while i < m:
            l = None
            for s in strs:
                if l != None and s[i] != l:
                    return "".join(res)
                l = s[i]
            res.append(l)
            i += 1
        return "".join(res)