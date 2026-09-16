class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        smp = [0]*26
        for c in s1:
            smp[ord(c)-ord('a')] += 1

        l,r = 0,0
        buf = [0]*26

        while r < len(s2):
            cr = ord(s2[r])-ord('a')
            buf[cr] += 1
            while buf[cr] > smp[cr]:
                cl = ord(s2[l])-ord('a')
                buf[cl] -= 1
                l += 1
            if buf == smp:
                return True
            r += 1
        
        return False

