class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # Binary Search Solution O(log n)
        lenN = len(nums) // 2
        if nums[lenN] != target: 
            return False

        # find left index
        l_index = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                r = mid - 1
            else:
                l = mid + 1
        l_index = r + 1

        # find right index
        r_index = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                l = mid + 1
            else:
                r = mid - 1
        r_index = r

        r = r_index - l_index + 1
        return r > lenN