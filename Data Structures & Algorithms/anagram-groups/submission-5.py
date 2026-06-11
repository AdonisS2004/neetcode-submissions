class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = dict()
        for string in strs:
            string_hash = [0]*26
            for char in string:
                string_hash[ord(char)-ord('a')] += 1
            string_hash = tuple(string_hash)
            if string_hash not in anagram_map:
                anagram_map[string_hash] = []
            anagram_map[string_hash].append(string)
        return [value for _, value in anagram_map.items()]