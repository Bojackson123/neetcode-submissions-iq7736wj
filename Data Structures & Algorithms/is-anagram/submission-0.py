class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqS = Counter(s)
        freqT = Counter(t)

        for key, value in freqS.items():
            if key not in freqT or freqT[key] != value:
                return False
        return True