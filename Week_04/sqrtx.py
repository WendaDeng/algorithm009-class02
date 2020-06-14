class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x // 2 + 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            square = mid * mid
            if square > x:
                hi = mid -1
            else:
                lo = mid
        return lo
