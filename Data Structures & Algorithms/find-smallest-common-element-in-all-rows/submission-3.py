class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        def binarySearch(index, n):
            l, r = 0, len(mat[index]) - 1

            while l <= r:
                mid = (l + r) // 2

                if mat[index][mid] > n:
                    r = mid - 1
                elif mat[index][mid] < n:
                    l = mid + 1
                else:
                    return True
            return False
        
        for i in range(len(mat[0])):
            found_in_all = True
            for j in range(1, len(mat)):
                if not binarySearch(j, mat[0][i]):
                    found_in_all = False
                    break
            if found_in_all:
                return mat[0][i]
        return -1