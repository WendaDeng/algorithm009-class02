class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        if s[0] == '0': return 0
        # 使用动态规划，因为当前项只与前两项有关，所以使用常数空间
        pre, cur = 1, 1
        for i in range(1, n):
            tmp = cur
            if s[i] == '0': # 遇到 ’0‘，单独处理
                if s[i - 1] == '1' or s[i - 1] == '2':
                    cur = pre
                else:
                    return 0
            elif s[i - 1] == '1' or (s[i - 1] == '2' and '1' <= s[i] <= '6'):
                cur += pre
            pre = tmp
        return cur
