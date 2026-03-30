class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashM = Counter(nums)

        for value in hashM.values():
            if value > 1:
                return True
        return False
