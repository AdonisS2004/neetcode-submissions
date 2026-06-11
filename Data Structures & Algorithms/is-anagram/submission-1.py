class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashDict = {}
        for char in s:
            if char in hashDict:
                hashDict[char] += 1
            else:
                hashDict[char] = 1
        for char in t:
            if char not in hashDict:
                return False
            hashDict[char] -= 1
            if hashDict[char] == 0:
                del hashDict[char]

        return True if not hashDict else False