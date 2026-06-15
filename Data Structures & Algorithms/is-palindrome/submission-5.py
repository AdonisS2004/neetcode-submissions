class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_ascii = {
            'a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y',
            'z', '0', '1', '2', '3',
            '4', '5', '6', '7', '8', 
            '9'
        }
        n = len(s)
        s = s.lower()
        l, r = 0, n-1

        while l < r:
            while l < n and s[l] not in valid_ascii:
                l += 1
            while r > -1 and s[r] not in valid_ascii:
                r -= 1
            if l >= r:
                break
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True