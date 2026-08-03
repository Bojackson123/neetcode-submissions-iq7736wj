class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        for k, v in freq.items():
            if v >= n:
                return k         
        
        