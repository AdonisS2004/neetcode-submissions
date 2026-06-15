class Solution:
    def isPalindrome(self, s: str) -> bool:
        numbers = {
            '0', '1', '2', '3','4',
            '5', '6', '7', '8', '9'
        }
        letters = {
            'a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y',
            'z'
        }
        s = s.lower()
        s_mod = []
        for char in s:
            if char in letters or char in numbers:
                s_mod.append(char)
        l, r = 0, len(s_mod)-1
        while l < r:
            if s_mod[l] != s_mod[r]:
                return False
            l += 1
            r -= 1
        return True