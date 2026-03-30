class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        flatArr = [item for sublist in matrix for item in sublist]
        low, high = 0, len(flatArr) - 1
        indexRes = -1

        while low <= high:
            mid = (low + high) // 2

            if flatArr[mid] > target:
                high = mid - 1
            elif flatArr[mid] < target:
                low = mid + 1
            else:
                indexRes = mid
                break
        
        if indexRes == -1:
            return False
        else:
            return True