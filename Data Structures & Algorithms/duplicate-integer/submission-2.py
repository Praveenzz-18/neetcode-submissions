class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        nums.sort()
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]:
                return True
        return False