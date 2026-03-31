class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Hashmap Solution O(n + m)
        seen = set(nums1)

        res = []
        for num in nums2:
            if num in seen:
                res.append(num)
                seen.remove(num)
        
        return res