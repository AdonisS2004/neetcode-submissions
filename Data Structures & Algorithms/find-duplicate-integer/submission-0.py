class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = [0]*10000
        node = nums
        for num in nums:
            if count[num] > 0:
                return num
            count[num] += 1