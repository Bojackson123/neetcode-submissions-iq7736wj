class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Two Pointer Solution
        if k == 0: return 0
        l, r = 0, 0
        res = 0
        total = 1

        while l <= r and r < len(nums):
            total *= nums[r]
            while total >= k and l <= r:
                total /= nums[l]
                l += 1
            res += r - l + 1
            r += 1
        return res
            
            