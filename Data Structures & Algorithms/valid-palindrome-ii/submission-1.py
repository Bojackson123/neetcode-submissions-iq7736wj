class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for i in range(len(s)):
            if isPal(s[:i] + s[i + 1:]):
                return True
        return False





    