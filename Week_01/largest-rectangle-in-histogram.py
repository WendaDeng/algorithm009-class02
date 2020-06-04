class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # base case
        if len(heights) == 0: return 0

        # add sentinel
        heights.append(0)
        max_area = 0
        idxs = [0]
        for i in range(1, len(heights)):
            while len(idxs) > 0 and heights[i] < heights[idxs[-1]]:
                height = heights[idxs[-1]]
                idxs.pop()
                left_idx = idxs[-1] if len(idxs) > 0 else -1
                max_area = max(max_area, height * (i - left_idx - 1))
            idxs.append(i)
        return max_area
