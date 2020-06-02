class Solution {
public:
    vector<string> res;

    vector<string> generateParenthesis(int n) {
        addParenthesis("", n, n);
        return res;
    }

    void addParenthesis(string s, int left, int right) {
        if (left == 0 && right == 0) {
            res.push_back(s);
            return;
        }
        if (left != 0) addParenthesis(s + "(", left - 1, right);
        if (right > left) addParenthesis(s + ")", left, right - 1);
    }
};
