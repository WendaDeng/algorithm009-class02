class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        if (nums.size() == 0) return;

        int j = 0;
        for (int i = 0; i < nums.size(); ++i)
            if (nums[i]) nums[j++] = nums[i];

        for (int i = j; i < nums.size(); ++i)
            nums[i] = 0;
    }
};
