class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # Brute Force Solution  O(n)
        l = len(nums) // 2
        freq = Counter(nums)
        return  target in freq and freq[target] > l