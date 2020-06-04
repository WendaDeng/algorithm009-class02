class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        if (nums.size() * k == 0) return res;
        if (k == 1) return nums;

        deque<int> window;
        for (int i = 0; i < k; i++) {
            // 每次将新的下标加入队列前都将其跟队列最后面的下标对应的元素进行比较
            // 这样可以保证队列中下标对应的元素是从大到小的
            while (!window.empty() && nums[i] > nums[window.back()])
                window.pop_back();
            window.push_back(i);
        }
        res.push_back(nums[window.front()]);

        for (int i = k; i < nums.size(); i++) {
            // 判断队头下标是否应该弹出
            if (!window.empty() && window.front() <= i - k)
                window.pop_front();
            while (!window.empty() && nums[i] > nums[window.back()])
                window.pop_back();
            window.push_back(i);
            // 每次取出对头下标对应的元素
            res.push_back(nums[window.front()]);
        }
        return res;
    }
};
