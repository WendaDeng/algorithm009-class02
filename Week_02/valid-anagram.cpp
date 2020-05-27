class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())   return false;

        // 使用数组(速度更快，但是无法适用于Unicode字符的情况)
        // int counts[26] = {0};
        // for (int i = 0; i < s.size(); ++i) {
        //     ++counts[s[i] - 'a'];
        //     --counts[t[i] - 'a'];
        // }

        // for (int i = 0; i < 26; ++i)
        //     if (counts[i])   return false;

        // 使用哈希表(速度慢一些，但是可以使用与Unicode字符情况)
        unordered_map<char, int> counts;
        for (int i = 0; i < s.size(); ++i) {
            ++counts[s[i]];
            --counts[t[i]];
        }

        for (auto count : counts)
            if (count.second) return false;

        return true;
    }
};
