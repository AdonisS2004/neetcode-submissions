class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for r in res[::]:
                res.append(r+[num])
        return res