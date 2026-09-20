class Solution:
    def numSquares(self, n: int) -> int:
        """
        S - m[i] is the least number of perfect square numbers that sum to n
        R - 
        T - 
        B - m[i] = 1 for every 
        O - res = m[n]
        T - 
        """
        m = [sys.maxsize]*(n+1)
        m[0] = 0
        p_sq = []
        for i in range(1, n+1):
            sq = i*i
            if sq > n:
                break
            m[sq] = 1
            p_sq.append(sq)

        for i in range(n+1):
            for sq in p_sq:
                if sq > i:
                    break
                m[i] = min(m[i-sq] + 1, m[i])

        print(m)
        
        return m[n] if m[n] != sys.maxsize else -1
