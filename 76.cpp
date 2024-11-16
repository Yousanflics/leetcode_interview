/*
Slide window

string 是 ascii 编码一共就 128 中，所以可以声明一个 size 是 128 的 int 数组
*/
// 以下是运行时间最快解
class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> letterCnt(128) =  {0};
        int left = 0, cnt = 0; minLeft = -1; minLen = INT_MAX;
        for(char c : t) ++letterCnt[c];
        for(int i = 0; i < s.size(), ++i) {
            if(--letterCnt[s[i]] >= 0) ++cnt;
            while(cnt == t.size) {
                if(minLen > i - left + 1) {
                    minLen = i - left + 1;
                    minLeft = left;
                }
                if(++letterCnt[s[left]] > 0) --cnt;
                ++left;
            }
        }
        return minLeft == -1 ? "" : s.substr(minLeft, minLen);
    }
};
