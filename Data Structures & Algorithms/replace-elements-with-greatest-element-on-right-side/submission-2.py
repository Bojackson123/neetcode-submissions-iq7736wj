class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Brute Force Solution O(n^2)
        for i in range(len(arr)):
            x = -1
            for j in range(i + 1, len(arr)):
                x = max(arr[j], x)
            arr[i] = x
        
        return arr