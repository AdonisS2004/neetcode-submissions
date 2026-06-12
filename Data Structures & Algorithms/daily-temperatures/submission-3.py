class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        warmest = 0
        stack = []
        for temp in temperatures[::-1]:
            if temp >= warmest:
                stack.append([temp, 0])
                warmest = temp
                res.append(0)
                continue
            count = 1
            while temp >= stack[-1][0]:
                count += stack[-1][1]
                stack.pop()
            res.append(count)
            stack.append([temp, count])
        return res[::-1]
            