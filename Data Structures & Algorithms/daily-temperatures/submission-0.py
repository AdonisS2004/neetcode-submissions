class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0 for _ in range(n)]
        stack = []
        idx = n-1
        while idx > -1:
            if not stack:
                res[idx] = 0
                stack.append(idx)
                idx -= 1
                continue
            while stack:
                cidx = stack.pop()
                if temperatures[idx] < temperatures[cidx]:
                    res[idx] += cidx - idx
                    stack.append(cidx)
                    break
            stack.append(idx)
            idx -= 1

        return res