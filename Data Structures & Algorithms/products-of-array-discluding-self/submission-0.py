class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * (len(nums) + 1)
        right = [1] * (len(nums) + 1)
        ans = []

        for i in range(len(nums)):
            left[i + 1] =  left[i] * nums[i]
        
        for i in range(len(nums) -1, -1, -1):
            right[i] = right[i + 1] * nums[i]

        print(left)
        print(right)
        
        for i in range(len(nums)):
            ans.append(left[i] * right[i + 1] )
        return ans