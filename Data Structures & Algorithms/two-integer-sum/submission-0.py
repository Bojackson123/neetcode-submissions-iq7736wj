class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffD = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in diffD:
                return [diffD[nums[i]], i]
            else:   
                diffD[diff] = i
        
        