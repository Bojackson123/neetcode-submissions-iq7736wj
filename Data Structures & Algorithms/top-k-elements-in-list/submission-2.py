class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqDict = defaultdict(int)
        for num in nums:
            freqDict[num] += 1
        
        sortedArr = sorted(freqDict.keys(), key=lambda x: freqDict[x], reverse=True)

        return sortedArr[:k]
