class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Brute Force O(N^2) Solution
        res = 1000
        for n in nums:
            res = min(res, n)
        
        return res