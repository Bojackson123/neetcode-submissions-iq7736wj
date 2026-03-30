class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Sort Array
        nums.sort()
        # Loop to find first number in triplet
        for i, a in enumerate(nums):
            # if the smallest number is greater then 0 we can return as no triplet will = 0
            if a > 0:
                break
            # if the current a is the same value as the previous we can skip it to avoid duplicates
            if i > 0 and a == nums[i -1]:
                continue
            # Set up the left and right pointers to find the 2nd and 3rd numbers (like Two Sum II)
            l, r = i + 1, len(nums) - 1
            while l < r:
                # Conditionals to tell which pointer to move. L if threeSum < 0, R if its > 0.
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # If the triplet = 0, append to results and incerment the pointers.
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # move L pointer right if it = its previous number to avoid duplicates. 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res


