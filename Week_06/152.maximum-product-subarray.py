class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:  return 0
        pre_max, pre_min, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            mx, mn = pre_max, pre_min
            pre_max = max(mx * nums[i], mn * nums[i], nums[i])
            pre_min = min(mx * nums[i], mn * nums[i], nums[i])
            res = max(res, pre_max)
        return res
