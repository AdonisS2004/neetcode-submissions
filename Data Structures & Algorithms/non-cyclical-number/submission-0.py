class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {n}
        num = n
        while  num != 1:
            next_num = 0
            while num != 0:
                next_num += (num%10)**2
                num = num//10
            if next_num in visited:
                return False
            visited.add(next_num)
            num = next_num
        return True