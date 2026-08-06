class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        tuples = [(-count, key) for key, count in freq.items()]
        heapq.heapify(tuples)

        res = []
        for i in range(k):
            res.append(heapq.heappop(tuples)[1])

        return res

        
        
        