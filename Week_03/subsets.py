class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 迭代解法，每次往已有结果中加入新元素，构成新的子集，然后跟原有子集合并
        # res = [[]]
        # for num in nums:
        #     res += [[num] + item for item in res]
        # return res

        # 回溯解法
        def backtrack(first = 0, curr = []):
            # terminator
            if len(curr) == k:
                # use curr[:] instead of curr
                output.append(curr[:])
            for i in range(first, n):
                # process current level logic
                curr.append(nums[i])
                # drill down
                backtrack(i + 1, curr)
                # reverse state
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
