from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l,r,n = 0,0,len(nums)
        if n <= k:
            return [max(nums)]
        
        window_array = deque([])
        while r < k:
            window_array.append(nums[r])
            r += 1

        while r < n:
            res.append(max(window_array))
            window_array.popleft()
            window_array.append(nums[r])
            r += 1
            
        res.append(max(window_array))
        return res