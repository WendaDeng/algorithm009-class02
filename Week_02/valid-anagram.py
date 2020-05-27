class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):    return False

        # 使用哈希表（即Python中的字典），可以适用于Unicode字符的情况
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            if c not in count: return False
            # 一开始没有下面的判断，结果出错了
            if count[c] <= 0:   return False
            count[c] = count[c] - 1
        return True
