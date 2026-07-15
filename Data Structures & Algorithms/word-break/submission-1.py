class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n, m, t = len(s), len(wordDict), max([len(w) for w in wordDict])
        memo = [False]*n
        for i in range(n):
            for j in range(t):
                if i-1 >= 0 and not memo[i-1]:
                    break 
                if i+j < n and s[i:i+j+1] in wordDict:
                    memo[i+j] = True
        return memo[-1]