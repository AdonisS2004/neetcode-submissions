class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i, size = 0, nums[0]
        res = 0
        while i < n-1:
            # base cases
            if i == n-1:
                break
            if i + size >= n-1:
                res += 1
                break
            
            next_i, next_size = i, size
            for j in range(i+1, i+size+1):
                if j + nums[j] > next_i + next_size:
                    next_i, next_size = j, nums[j]
            i, size = next_i, next_size
            res += 1
        return res