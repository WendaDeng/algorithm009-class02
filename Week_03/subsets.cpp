class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        // 需要显示初始化为空
        vector<vector<int>> res = {{}};
        if (nums.size() == 0)   return res;
        for (int num : nums) {
            int size = res.size();
            for (int i = 0; i < size; i++) {
                // 先把当前遍历的元素加入 vector 尾部，然后对齐进行拓展
                res.push_back(res[i]);
                res.back().push_back(num);
            }
        }
        return res;
    }
};
