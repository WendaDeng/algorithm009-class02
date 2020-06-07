class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        if (n <= 0 || k <= 0) return res;
        vector<int> nums;
        backtrack(nums, 1, n, k);
        return res;
    }
private:
    vector<vector<int>> res;

    void backtrack(vector<int> &nums, int start, int n, int k) {
        // terminator
        if (nums.size() == k) {
            res.push_back(nums);
            return;
        }
        // use backtrack
        for (int i = start; i <= n; ++i) {
            nums.push_back(i);
            backtrack(nums, i + 1, n, k);
            nums.pop_back();
        }
    }
};
