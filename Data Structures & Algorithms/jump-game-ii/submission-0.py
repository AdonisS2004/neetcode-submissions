class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i, size = 0, nums[0]
        minJumps = 0
        while i < n-1:
            print(i, size)
            if i + size >= n-1:
                if i != n-1:
                    minJumps += 1
                break
            
            next_i, next_size = i, size
            for j in range(i+1, i+size+1):
                # bigger window
                if j + nums[j] > next_i + next_size:
                    next_i, next_size = j, nums[j]
            i, size = next_i, next_size
            minJumps += 1
        return minJumps