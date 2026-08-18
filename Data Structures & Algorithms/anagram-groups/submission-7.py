class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strategy: create a hash with each string using the letters
        anagrams = dict()

        for s in strs:
            hash = [0]*26
            for c in s:
                hash[ord(c)-ord('a')] += 1
            hash = tuple(hash)
            if hash not in anagrams:
                anagrams[hash] = []
            anagrams[hash].append(s)
        
        res = list(anagrams.values())
        return res