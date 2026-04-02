class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # Two Pointer Solution
        if len(nums) < 3: return 0
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                sum_x = nums[l] + nums[r]

                if sum_x < target - nums[i]:
                    count += r - l
                    l += 1
                else:
                    r -= 1
        return count