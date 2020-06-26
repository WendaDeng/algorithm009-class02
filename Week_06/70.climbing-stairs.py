class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:  return 1
        if n <= 2:  return n
        n1, n2 = 1, 2
        for i in range(3, n+1):
            n1, n2 = n2, n1 + n2
        return n2
