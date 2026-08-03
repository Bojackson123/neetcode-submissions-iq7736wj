class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        res, max_count = 0, 0
        for num in nums:
                freq[num] += 1
                if max_count < freq[num]:
                    res = num
                    max_count = freq[num]
        return res
        
        