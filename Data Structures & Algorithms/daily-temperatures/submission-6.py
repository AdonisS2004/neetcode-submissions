class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        
        n = len(temperatures)
        res = [0]*n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                j = stack[-1]
                res[i] = j-i
            stack.append(i)

        return res