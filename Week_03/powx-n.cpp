class Solution {
public:
    double myPow(double x, int n) {
        long long N = n;

        return N >= 0 ? quickMul(x, N) : 1.0 / quickMul(x, -N);
    }

    double quickMul(double x, long long n) {
        // terminator
        if (n == 0) return 1;
        // current level logic, drill down, combine result
        double res = quickMul(x, n / 2);
        return n & 1 ? res * res * x : res * res;
    }
};
