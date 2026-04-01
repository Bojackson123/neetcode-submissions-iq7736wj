class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # Brute Force Solution
        freqDict = defaultdict(int)
        n = len(mat)
        res = 0

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                freqDict[mat[i][j]] += 1
        print(freqDict)
        
        for k, v in freqDict.items():
            if v == n:
                return k
        return -1
        