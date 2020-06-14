class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:  return nums[0]
        lo, hi = 0, len(nums) - 1
        if nums[hi] > nums[lo]: return nums[lo]

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[lo] < nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
