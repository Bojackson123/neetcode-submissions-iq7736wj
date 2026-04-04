class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if l == r: return nums[l]
            mid = (l + r) // 2

            # Even case
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    l = mid + 1
                elif nums[mid] != nums[mid - 1]:
                    return nums[mid]
                else:
                    r = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1
                elif nums[mid] != nums[mid + 1]:
                    return nums[mid]
                else:
                    r = mid - 1
        