class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(N^2) Solution
        res = [0] * len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            res[i] = product
        
        return res
        