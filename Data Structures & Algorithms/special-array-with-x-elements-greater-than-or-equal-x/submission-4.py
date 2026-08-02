class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def getCount(index, arr):
            count = 0
            for ele in arr:
                if ele >= index:
                    count += 1
            return count

        nums.sort()
        l, r = 0, len(nums)

        while l <= r:
            mid = (r + l) // 2
            count = getCount(mid, nums)
            
            if count > mid:
                l = mid + 1
            elif count < mid:
                r = mid - 1
            else:
                return mid

            
        return -1
