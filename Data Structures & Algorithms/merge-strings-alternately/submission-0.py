class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = len(word1) if len(word1) >= len(word2) else len(word2)
        res = []

        for i in range(l):
            if i < len(word1):
                res.append(word1[i])
            if i < len(word2):
                res.append(word2[i])

        return "".join(res)
                
            