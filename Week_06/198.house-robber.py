class Solution:
    def rob(self, nums: List[int]) -> int:
        # 动态规划，使用一个 dp 数组，其中 dp[i] 表示到第 i 间为止，抢到的最大金额
        # if len(nums) == 0:  return 0
        # n = len(nums)
        # dp = [0] * (n+1)
        # dp[1] = nums[0]
        # for i in range(2, n+1):
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        # return dp[-1]

        # 因为当前值，只跟前两个值有关，所以可以进一步压缩至O(1)的时间复杂度
        pre, cur = 0, 0
        for num in nums:
            tmp = max(cur, pre + num)
            pre, cur = cur, tmp
        return cur
