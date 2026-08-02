class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()
        l, r = 0, len(nums)

        while l <= r:
            mid = (r + l) // 2
            count = 0
            for num in nums:
                if num >= mid:
                    count += 1
            
            if count > mid:
                l = mid + 1
            elif count < mid:
                r = mid - 1
            else:
                return mid

            
        return -1
