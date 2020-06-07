### 学习笔记

本周学习的内容是递归、分治和回溯。这些内容在本科学习算法和数据结构的时候都曾学过。但是我从来没有真正掌握，对这些算法属于一知半解的状态。但既然花钱购买了课程，这次我一定要攻克这些算法。

具体做的第一步肯定是先看视频，听听覃超老师的讲解。课程中覃超老师总结了解决递归问题的四个步骤：
1.  terminator
2.  process current level logic
3.  drill down
4.  reverse state

有了这个解题框架后，无论是做题还是看别人的题解，心里都有谱了。这四个步骤中最重要的是**步骤1：terminator（终止条件）**，如果没有这个步骤，递归就会陷入死循环！虽然覃超老师在视频中反复强调，但是我自己在写代码的过程中仍然犯了几次忘了写终止条件的错误。之后才养成每次首先思考终止条件的习惯。

这里还需要提一下的是步骤4：reverse state（状态恢复）。这个步骤并不是所有的递归程序都必须的，这需要看你传入的参数，以及在递归体中是如何进行判断的。比如**括号生成**问题中，我们可以通过传入的参数控制剩余可用的左括号和右括号的数量，然后在递归体中进行判断，这样就不需要进行状态恢复。



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


但是在下面的**组合**问题中，因为传入的参数 *k* 并没有在递归体中改变过，相应的终止条件也是假设 *k* 不变的，所以我们需要在递归（回溯）之后恢复状态。


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


在本周的学习之前，我并未将回溯与递归在一起。但是经过本周的学习，我知道其实回溯依赖于递归，或者说回溯是一种特殊的递归。其特殊之处就是每次递归开始前，我们先要改变传入参数的状态，而递归完之后则需要恢复参数的状态。了解了回溯的特点之后，解决起问题就容易多了，以前视若猛虎的**N皇后**问题也能够比较轻松地理解并自己实现了。

此外，在题解去看到了 **labuladong** 总结的回溯问题的[套路](https://leetcode-cn.com/problems/n-queens/solution/hui-su-suan-fa-xiang-jie-by-labuladong/)，强调 **路劲** 和 **状态** ，路径就是我们已经做过的选择，而状态则是我们剩下还能做的选择。这个思路使我非常受益，结合覃超老师讲解的四个步骤，进一步加深了对回溯算法的理解。

这周算是在攻克回溯算法的路上踏出了第一步，接下来还要多思考、多练习，进一步加深自己对回溯（递归）算法的理解，提升自己的熟练读。






















