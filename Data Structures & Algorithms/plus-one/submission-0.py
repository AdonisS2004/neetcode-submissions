class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = digits[::]
        idx = len(digits)-1
        while carry and idx >= 0:
            res[idx] += carry
            carry = res[idx]//10
            res[idx] %= 10
            idx -= 1
        return res if carry == 0 else [carry] + res