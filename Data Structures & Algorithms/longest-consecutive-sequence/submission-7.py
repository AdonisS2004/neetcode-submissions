class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nm = defaultdict(int)
        res = 0
        for num in nums:
            if not nm[num]:
                nm[num] = nm[num-1] + nm[num+1] + 1
                nm[num - nm[num-1]] = nm[num]
                nm[num + nm[num+1]] = nm[num]
                res = max(res, nm[num])
        return res