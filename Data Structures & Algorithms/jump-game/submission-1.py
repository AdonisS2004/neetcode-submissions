class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        canReach = {n-1}
        i = n-2
        while i >= 0:
            for offset in range(nums[i]+1):
                if i + offset in canReach:
                    canReach.add(i)
                    break
            i-=1
        return True if 0 in canReach else False