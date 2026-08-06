class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3

        res = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
            if freq[num] == n + 1:
                res.append(num)
        return res