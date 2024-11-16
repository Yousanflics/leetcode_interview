class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams;
        for(const &str : strs) {
            string key = str;
            str.sort(str.begin(), str.end());
            anagrams[key] = str;
        }

        vector<vector<string>> res;
        for(auto &entry : anagrams) {
            res.push_back(entry.second);
        }
        retrun res;
    }
};
