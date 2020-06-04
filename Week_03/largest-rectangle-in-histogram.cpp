class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int res = 0;
        if (heights.size() == 0)    return res;

        heights.push_back(0);   // sentinel，用于弹出处理最后一个元素
        vector<int> index;
        for (int i = 0; i < heights.size(); ++i) {
            while (index.size() > 0 && heights[index.back()] > heights[i]) {
                int h = heights[index.back()];
                index.pop_back();
                int leftbound = index.size() > 0 ? index.back() : -1;
                res = max(res, (i - leftbound - 1) * h);
            }
            index.push_back(i);
        }
        return res;
    }
};
