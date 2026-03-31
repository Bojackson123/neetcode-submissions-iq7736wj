class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Brute Force O(N^2) Solution
        res = set()
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    res.add(nums2[j])
        
        return list(res)