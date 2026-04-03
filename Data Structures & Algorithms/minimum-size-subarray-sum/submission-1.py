class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0

        l, r = 0, 0
        res = 100_000
        total = 0

        while r < len(nums):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1
        return res