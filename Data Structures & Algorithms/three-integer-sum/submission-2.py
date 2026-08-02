class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        results = []

        for fixed in range(n):
            if fixed > 0:
                if nums[fixed] == nums[fixed - 1]:
                    continue

            lo, hi = fixed + 1, n - 1

            while lo < hi:
                if nums[fixed] + nums[lo] + nums[hi] > 0:   # Case Greater Than Zero
                    hi -= 1
                elif nums[fixed] + nums[lo] + nums[hi] < 0: # Case Less Than Zero
                    lo += 1
                else:                                 # Case Match
                    # Append to results
                    results.append((nums[fixed], nums[lo], nums[hi]))
                    # Iterate passed the duplicates (lo)
                    curr_lo = nums[lo]
                    while lo < hi and nums[lo] == curr_lo:
                        lo += 1

                    # Interate Passed the duplicated (hi)
                    curr_hi = nums[hi]
                    while lo < hi and nums[hi] == curr_hi:
                        hi -= 1

        return results



























































































































       