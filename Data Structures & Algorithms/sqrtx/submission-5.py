class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary Search Solution O(log n)
        if x == 0:
            return 0
        res = 1

        l, r = 1, x + 1
        res = 1
        while l <= r:
            mid = (r + l) // 2

            if mid * mid > x:
                r = mid - 1
                res = r
            elif mid * mid < x:
                l = mid + 1 
            else:
                return mid
        return res