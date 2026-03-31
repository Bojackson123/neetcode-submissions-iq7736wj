class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        lastPos = 0
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target:
                lastPos = mid
                r = mid - 1
            elif nums[mid] < target:
                lastPos = mid + 1
                l = mid + 1
            else:
                return mid
        return lastPos