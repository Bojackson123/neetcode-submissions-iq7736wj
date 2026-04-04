class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        print(s)
        parts = s.split(" ")
        return len(parts[-1])