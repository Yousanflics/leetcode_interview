/*
最长有效括号

题目分析：
首先可以联想 20 Valid Parentheses 显然这个似乎更大一点，同时括号的话可以联想到前缀转后缀的时候case，所以这里考虑下用栈来求解
思路分析：
需要定义个 start 变量来记录合法括号串的起始位置，遍历字符串，如果遇到左括号，则将当前下标压入栈
- 如果遇到右括号，如果当前栈为空，则将下一个坐标位置记录到 start，因为没有匹配上所以直接 jump 到下一个
- 如果栈不为空，则将栈顶元素取出，此时若栈为空，则更新结果和 i - start + 1 中的较大值，否则更新结果和 i - st.top() 中的较大值
难点分析：
- why +1，另一个没有呢？其实这就是一个坐标的问题，start 指向的是有效括号的起始位置，那么算长度的时候就要加一，比如对于 "()" 来说，此时 start=0，i=1，那么长度就是 i-start+1 = 2。
- 栈顶元素表示的是有效括号的前一个位置，就比如说对于 "(()" 来说，此时栈顶元素是第一个左括号的位置，即0，而 i=2，由于第一个左括号不在有效括号长度中，所以就是直接 i-st.top()=2
- 总结：本质难点还是考虑使用 stack 去模拟匹配过程同时计算长度的时候考虑到 index 相关的问题是否需要 +1 来计算准确的长度
*/

// 也是用时最短的 solution
class Solution {
public:
    int longestValidParentheses(string s) {
        int res = 0; start = 0, n = s.size();
        //st 是记录下标的
        stack<int> st;
        for(int i = 0; i < n; i++) {
            if(s[i] == '(') st.push(i);
            else if (s[i] == ')') {
                if(st.empty()) {
                    //如果当前stack中还是 empty 的话那就往后稍一稍， i + 1 找下一个
                    start = i + 1;
                } else {
                    st.pop();
                    res = st.empty() ? max(res, i - start + 1) : max(res, i - st.top());
                }
            }
        }
        return res;
    }
};
