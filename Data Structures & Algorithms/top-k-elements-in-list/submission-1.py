class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        ans = []
        for i in range(k):
            largest = 0
            keyL = 0
            for key, value in freq.items():
                if value > largest:
                    largest = value
                    keyL = key
            ans.append(keyL)
            freq[keyL] = 0
        return ans