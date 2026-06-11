class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            size = len(string)
            encoded_string = encoded_string + str(size) + "#" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        size = len(s)
        idx = 0
        res = []
        while idx < size:
            start = idx
            while s[idx] != "#":
                idx += 1
            str_size = int(s[start:idx])
            string = ""
            idx += 1
            while str_size > 0:
                string = string + s[idx]
                idx += 1
                str_size -= 1
            res.append(string)
        return res
