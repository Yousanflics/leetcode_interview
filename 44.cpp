/*
WildCard Matching
在 s 中匹配 p
*/

Class Solution {
public:
    bool isMatch(string s, string p) {
        int i = 0, j = 0, istar = -1, jstar = -1, m = s.size(), n = p.size();
        while(i < m) {
            // 主要操作是对 s 遍历的时候需要处理 p 不同字符的匹配问题
            if(j < n &&(s[i] == p[j] || p[j] == '?')) {
                ++i; ++j;
            } else if (j < n && p[j] == '*') {
                istar = i;
                jstar = j++;
            } else if (istar >= 0) {
                i = ++istar;
                j = jstar + 1;
            } else return false;
        }
        while(j < n && p[j] == '*') ++j;
        return j == n;
    }
};
