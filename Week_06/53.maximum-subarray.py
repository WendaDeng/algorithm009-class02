class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_sum, res = 0, nums[0]
        for i in range(len(nums)):
            pre_sum = max(0, pre_sum) + nums[i]
            res = max(pre_sum, res)
        return res
