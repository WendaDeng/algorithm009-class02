class Solution:
    def rob(self, nums: List[int]) -> int:
        # 沿用打家劫舍1的解题思路，但为了解决环形带来的问题，可以将环拆分成两个错开的单向数组
        # 即将nums 拆分成 nums[:-1](不包含最后一个房子) 和 nums[1:](不包含第一个房子)
        def my_rob(nums):
            pre, cur = 0, 0
            for num in nums:
                pre, cur = cur, max(cur, pre + num)
            return cur
        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]
