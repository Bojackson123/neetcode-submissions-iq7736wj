class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # Binary Search on the rows to find which row could possibly contain out anwser.
        row_l = 0
        row_h = ROWS - 1
        rowRes = -1

        while row_l <= row_h:
            m = (row_l + row_h) // 2

            if matrix[m][0] <= target and matrix[m][COLS - 1] >= target:
                rowRes = m
                break
            elif matrix[m][COLS - 1] < target:
                row_l = m + 1
            else:
                row_h = m - 1
        
        # Return False early if we don't find a suitable row.
        if rowRes == -1: 
            return False

        # Now we do normal binary search on the correct row
        low = 0
        high = COLS - 1
        colRes = -1

        while low <= high:
            mid = (high + low) // 2

            if matrix[rowRes][mid] < target:
                low = mid + 1
            elif matrix[rowRes][mid] > target:
                high = mid - 1
            else:
                colRes = mid
                break

        if colRes == -1:
            return False
        else:
            return True