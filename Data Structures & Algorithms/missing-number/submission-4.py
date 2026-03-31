class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Brute Force Solution O(n)
        nums.sort()
        count = 0

        for i in range(len(nums)):
            if nums[i] != count:
                return count
            count += 1
        return count