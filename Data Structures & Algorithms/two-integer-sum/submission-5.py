class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in target_map:
                return [target_map[diff], i]
            if nums[i] not in target_map:
                target_map[nums[i]] = i
        return []