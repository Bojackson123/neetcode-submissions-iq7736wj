class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Brute Force Solution O(N)

        for i in range(1, num + 1):
            sq = i * i
            if sq > num:
                return False
            if sq == num:
                return True