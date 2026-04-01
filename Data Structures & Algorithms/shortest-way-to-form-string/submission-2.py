class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # Two Pointers
        s, t = 0, 0
        res = 0

        while t < len(target):
            # Check if character is even in source
            if target[t] not in source:
                return -1
            
            if s == 0:
                res += 1
            
            if source[s] == target[t]:
                t += 1
            
            s += 1
            if s == len(source):
                s = 0

        return res