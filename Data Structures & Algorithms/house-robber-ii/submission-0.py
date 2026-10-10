class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def rob_liner(nums:List[int])-> int:
            rob1, rob2=0,0
            for n in nums:
                maxRob=max(n+rob2, rob1)
                rob2=rob1
                rob1=maxRob
            return rob1
        return max(rob_liner(nums[:-1]), rob_liner(nums[1:]))