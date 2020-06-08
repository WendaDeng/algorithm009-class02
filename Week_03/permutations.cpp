class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        if (nums.empty())   return res;
        vector<int> track;
        // 使用一个数组来判断某个数是否已经被使用
        vector<bool> contain(nums.size(), false);
        backtrack(nums, track, contain);
        return res;
    }
private:
    vector<vector<int>> res;

    void backtrack(vector<int> & nums, vector<int> &track, vector<bool> &contain) {
        if (track.size() == nums.size()) {
            res.push_back(track);
            return;
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (!contain[i]) {
                // 设置状态
                track.push_back(nums[i]);
                contain[i] = true;
                // 递归进入下一层
                backtrack(nums, track, contain);
                // 恢复状态
                track.pop_back();
                contain[i] = false;
            }
        }
    }
};
