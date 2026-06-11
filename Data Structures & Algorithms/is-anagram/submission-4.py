class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict()
        for char in s:
            if char not in s_map:
                s_map[char] = 0
            s_map[char] += 1

        for char in t:
            if char not in s_map:
                return False
            if s_map[char] == 0:
                return False
            s_map[char] -= 1
        
        for _, value in s_map.items():
            if value > 0:
                return False
         
        return True