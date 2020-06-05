class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 采用内部函数，代码更加紧凑
        def quickMul(n: int) -> float:
            # terminator
            if n == 0: return 1.0
            # current logic and drill down
            # 这里必须使用 '//' 运算符，结果才是 int，使用 '/' 运算符结果为 float
            res = quickMul(n // 2)
            # combine results
            return res * res if n % 2 == 0 else res * res * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
