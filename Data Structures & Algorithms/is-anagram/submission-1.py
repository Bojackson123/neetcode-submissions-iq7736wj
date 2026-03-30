class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)

        for c in s:
            freq_s[c] += 1
        
        for c in t:
            freq_t[c] += 1

        for k,v in freq_s.items():
            if k not in freq_t or freq_s[k] != freq_t[k]:
                return False
        
        return True
        