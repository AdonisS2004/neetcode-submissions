class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        v = set()
        for num in nums:
            if num in v:
                return True
            v.add(num)
        return False