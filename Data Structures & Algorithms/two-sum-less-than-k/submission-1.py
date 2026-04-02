class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # Two Pointer Solution
        nums.sort()
        l, r = 0, len(nums) - 1
        res = -1
        while l < r:
            sum_x = nums[l] + nums[r]
            if sum_x < k:
                res = max(res, sum_x)
                l += 1
            elif sum_x >= k:
                r -= 1
                            
        return res

            