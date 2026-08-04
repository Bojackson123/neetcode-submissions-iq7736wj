class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res_max = 0
        s, f = 0, 0
        zeros = 0

        while f < len(nums):
            if nums[f] == 0:
                zeros += 1
            
            if zeros > k:
                while zeros > k:
                    if nums[s] == 0:
                        zeros -= 1
                    s += 1
            res_max = max(res_max, f - s + 1)
            f += 1

        return res_max
