class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }

        vector<int> res;
        // 默认是大根堆
        priority_queue<pair<int, int>> pq;
        for (auto it = count.begin(); it != count.end(); it++) {
            // pair<first, second>: first is frequency, second is number
            pq.push(make_pair(it->second,  it->first));
            // 因为使用的是大根堆，所以维护的堆中节点数为 size - k
            if (pq.size() > count.size() - k) {
                res.push_back(pq.top().second);
                pq.pop();
            }
        }
        return res;
    }
};
