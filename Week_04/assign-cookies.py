class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(g) == 0 or len(s) == 0:  return 0
        g = sorted(g)
        s = sorted(s)
        content, i, j = 0, 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content += 1
                i += 1
            j += 1
        return content
