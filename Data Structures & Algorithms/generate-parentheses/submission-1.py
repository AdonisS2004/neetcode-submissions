class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(s,l,r):
            if l == n and r == n:
                res.append("".join(s))
                return
            if l < n:
                s.append('(')
                dfs(s,l+1,r)
                s.pop()
            if r < n and r < l:
                s.append(')')
                dfs(s,l,r+1)
                s.pop()
            return
        dfs([],0,0)
        return res