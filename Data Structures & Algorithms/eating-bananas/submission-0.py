class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            if self.eatingSpeed(k, piles) <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res

    def eatingSpeed(self, k, piles):
        total_time = 0
        for p in piles:
            total_time += math.ceil(float(p) / k)
        return total_time
