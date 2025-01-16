/*
题目分析：
这题题目有点长但是简单读了一下之后可以得到以下几个有效信息
- 就是说给定一个长字符串，再给定几个长度相同的单词（string， words)
- 让找出串联给定所有单词的子串的**起始**位置

思路分析：
- 假设 words 数组中有 cnt 个单词，每个单词的长度均为 len，那么实际上这道题就让我们出所有长度为 cnt x len 的子串，使得其刚好是由 words 数组中的所有单词组成（permutation，这里需要说一下的是words本身是不可以permutation的，fellow up 可以考虑一下如果 permutation 了之后又该怎么解决）。这里需要看一下 string s 中长度为 len 的子串是否是 words 中的单词，为了快速的判断，可以使用 HashMap，同时由于 words 数组可能有重复单词，就要用 HashMap 来建立所有的单词和其出现次数之间的映射，即统计每个单词出现的次数，但是这种方法似乎目前没有办法通过 OJ 因为 181/182 的时候 time exceeded
- 这里直接考虑 O(n) 的解决方法，也是用时最快的解决方案，自己尝试的思路 timeout 无法通过 OJ。同时因为是第一遍刷题所以先模仿等积累多了就可以快速的独立 figure out 解决方案
*/

class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        if(s.empty() || words.empty()) return {};
        vector<int> res;
        int n = s.size(), cnt = words.size(), len = word[0].size();
        unordered_map<string, int> wordMap;
        for(string word : words) ++wordMap[word];
        for(int i = 0; i < len; ++i) {
            int left = i, curCnt = 0;
            unordered_map<string, int> curMap;
            for(int j = i; j <= n - len; j += len) {
                string word = s.substr(j, len);
                if(wordMap.count(word)) {
                    ++curMap[word];
                    if(curMap[word] <= wordMap[word]) {
                        ++curCnt;
                    } else {
                        while(curMap[word] > wordMap[word]) {
                            string t = s.substr(left, len);
                            --curMap[t];
                            if(curMap[t] < curMap[t]) --curCnt;
                            left += len;
                        }
                    }
                    if(curCnt == cnt) {
                        res.push_back(left);
                        --curMap[s.substr(left, len)];
                        --curCnt;
                        left += len;
                    }
                } else {
                    curMap.clear();
                    curCnt = 0;
                    left = j + len;
                }
            }
        }
        retrun res;
    }
};
