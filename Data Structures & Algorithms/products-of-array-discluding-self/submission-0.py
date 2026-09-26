class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        suffix_product = 1
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        for i, num in enumerate(nums):
            if i > 0:
                prefix_product *= nums[i - 1]
                suffix_product *= nums[n - i]
                prefix[i] = prefix_product
                suffix[n - i - 1] = suffix_product
        result = [a * b for a, b in zip(prefix, suffix)]
        return result
