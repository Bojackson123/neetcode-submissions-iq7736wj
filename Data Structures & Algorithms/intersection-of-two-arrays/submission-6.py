class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Binary Search
        nums2.sort() # Only sort the arr that is being checked
        res = set()

        def binarySearch(n):
            l, r = 0, len(nums2) - 1

            while l <= r:
                mid = (r + l) // 2

                if nums2[mid] > n:
                    r = mid - 1
                elif nums2[mid] < n:
                    l = mid + 1
                else:
                    return nums2[mid]
            return -1
        
        for num in nums1:
            if num not in res:
                bs = binarySearch(num) 
                if bs != -1:
                    res.add(bs)
        return list(res)
