class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        n = len(sweetness)
        l, r = 0, sum(sweetness) // (k + 1)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            total = 0
            count = 0
            for num in sweetness:
                total += num
                if total >= mid:
                    count += 1
                    total = 0
            if count >= k + 1:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res
                