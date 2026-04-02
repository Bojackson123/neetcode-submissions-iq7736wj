class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # Brute Force Solution
        res = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum_x = nums[i] + nums[j]
                if sum_x < k:
                    res = max(res, sum_x)
        return res