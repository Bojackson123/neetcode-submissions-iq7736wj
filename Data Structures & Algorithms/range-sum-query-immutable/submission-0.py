class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_fix = []
        total = 0
        for num in nums:
            total += num
            self.pre_fix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.pre_fix[right]
        left_sum = self.pre_fix[left - 1] if left > 0 else 0
        return (right_sum - left_sum)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)