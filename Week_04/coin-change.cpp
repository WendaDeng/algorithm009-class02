class Solution {
public:
    // 贪心（快速找到可能解） + dfs + 回溯（保证找到最优解）
    int coinChange(vector<int>& coins, int amount) {
        if (coins.empty() || amount <= 0)   return 0;
        sort(coins.rbegin(), coins.rend());
        int ans = INT_MAX;
        coinChange(coins, amount, 0, 0, ans);
        return ans == INT_MAX ? -1 : ans;
    }
    void coinChange(vector<int> &coins, int amount, int c_index, int count, int &ans) {
        if (amount == 0) {
            ans = min(ans, count);  // 比较，选出最优解
            return;
        }
        if (c_index == coins.size()) return;

        // 当前币值（coins[c_index]）下，最多能取 k = amount / coins[c_index] 次
        // 如果不成功，则回溯（k--）
        for (int k = amount / coins[c_index]; k >= 0 && k + count < ans; k--) {
            coinChange(coins, amount - k * coins[c_index], c_index + 1, count + k, ans);
        }
    }
};
