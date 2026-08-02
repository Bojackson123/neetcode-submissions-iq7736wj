import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-weight for weight in stones]
        heapq.heapify(max_heap)
        
        while max_heap:
            if len(max_heap) == 1:
                return -max_heap[0]
            
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)

            if x > y:
                heapq.heappush(max_heap, -(x - y))
            
        
        return 0