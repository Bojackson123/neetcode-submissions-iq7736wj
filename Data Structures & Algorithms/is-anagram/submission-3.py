class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = Counter(s)
        t_freq = Counter(t)

        for k, v in s_freq.items():
            if k not in t_freq:
                return False
            if v != t_freq[k]:
                return False
        return True
        
        