class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        res = []
        n = len(nums) // 3
        for num in nums:
            if freq[num] > n:
                continue

            freq[num] += 1
            if freq[num] > n:
                res.append(num)
        return res
