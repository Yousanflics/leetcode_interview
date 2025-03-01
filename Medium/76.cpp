/*
Slide window

string 是 ascii 编码一共就 128 中，所以可以声明一个 size 是 128 的 int 数组
*/
// 以下是运行时间最快解
class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> letterCnt(128) = {0};
        int left = 0, cnt = 0, minLeft = -1, minLen = INT_MAX;
        for(const char & c : t) ++letterCnt[c];
        for(int i = 0; i < s.size(); ++i) {
            if(--letterCnt[s[i]] >= 0) ++cnt;
            // 缩小边界
            while(cnt == t.size()) {
                // 更新左边界&length
                if(minLen > i - left + 1) {
                    minLen = i - left + 1;
                    //left 起始为 0
                    minLeft = left;
                }
                //自增之后发现 > 0 说明回复了之后去除掉了本来有的元素，left可以++但是不能赋值给 minLeft 也正是因为 cnt != t.size() 了所以没法赋值
                if(++letterCnt[s[left]] > 0) --cnt;
                left++;
            }
        }
        return minLeft == -1 ? "":s.substr(minLeft, minLen);
    }
};
