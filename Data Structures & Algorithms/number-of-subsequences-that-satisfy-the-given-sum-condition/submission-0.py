class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Two-Pointer Solution
        MOD = 1000000007
        nums.sort()
        
        l, r = 0, len(nums) - 1
        res = 0

        while l <= r:
            sum_x = nums[l] + nums[r]
            if sum_x <= target:
                res = (res + pow(2, r - l, MOD)) % MOD
                l += 1
            else:
                r -= 1
        return res