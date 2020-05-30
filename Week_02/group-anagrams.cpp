class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string> > ans;
        if (strs.size() == 0)   return ans;

        int sub = 0;
        string tmp;
        unordered_map<string, int> work;
        for (auto str : strs) {
            tmp = str;
            sort(tmp.begin(), tmp.end());
            if (work.count(tmp)) {
                ans[work[tmp]].push_back(str);
            } else {
                vector<string> vec(1, str);
                ans.push_back(vec);
                work[tmp] = sub++;
            }
        }
        return ans;
    }
};
