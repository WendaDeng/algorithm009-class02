class Solution:
    def hammingWeight(self, n: int) -> int:
        if n < 0:  return -1
        result = 0
        while n:
            result += 1
            n = n & (n - 1)
        return result