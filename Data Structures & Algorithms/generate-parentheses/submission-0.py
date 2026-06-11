class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(l, r, n, curr):
            if l == r and l == n:
                res.append("".join(curr))
                return
            if l != n:
                curr.append("(")
                helper(l+1, r, n, curr)
                curr.pop()
            if r != n and r < l:
                curr.append(")")
                helper(l, r+1, n, curr)
                curr.pop()
            return
        helper(0,0,n,[])
        return res
