class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Two Pointer Solution O(N)
        nums1.sort()
        nums2.sort()
        print(nums1)
        print(nums2)
        res = set()

        l, r = 0, 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] > nums2[r]:
                r += 1
            elif nums1[l] < nums2[r]:
                l += 1
            else:
                res.add(nums2[r])
                r += 1
                l += 1
        
        return list(res)

