class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        l, r = 0, reader.length() - 1
        
        while l < r:
            length = (r - l + 1)
            mid = l + (length // 2)
            
            if length % 2 == 0:
                # Even length: compare [l, mid-1] and [mid, r]
                res = reader.compareSub(l, mid - 1, mid, r)
                if res == 1:
                    r = mid - 1
                else:
                    l = mid
            else:
                # Odd length: compare [l, mid-1] and [mid+1, r], mid is the middle element
                res = reader.compareSub(l, mid - 1, mid + 1, r)
                if res == 1:
                    r = mid - 1
                elif res == -1:
                    l = mid + 1
                else:
                    return mid
        return l