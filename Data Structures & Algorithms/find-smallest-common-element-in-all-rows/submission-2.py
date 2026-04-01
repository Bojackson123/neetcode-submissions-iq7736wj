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
        
        for i in range(len(mat[0])):
            if freqDict[mat[0][i]] == n:
                return mat[0][i]
        return -1