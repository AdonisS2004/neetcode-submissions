class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1]
        suffix_products = [1]

        # build prefix
        for num in nums[:len(nums)-1]:
            next_val = prefix_products[-1] * num
            prefix_products.append(next_val)

        # build suffix
        for num in nums[len(nums)-1:0:-1]:
            next_val = suffix_products[-1] * num
            suffix_products.append(next_val)
            
        return [x * y for x,y in zip(prefix_products, suffix_products[::-1])]