class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0: return True
        # forwards
        # m = 0
        # for i, n in enumerate(nums):
        #     if i > m:
        #         return False
        #     m =  max(m, i + n)
        # return True

        # backwards
        endReachable = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= endReachable:
                endReachable = i
        return not endReachable
