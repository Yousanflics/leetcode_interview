class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;
        int n = intervals.size(), cur = 0;
        while(cur < n && intervals[cur][1] < newInterval[cur][0]) {
            res.push_back(intervals[cur++]);
        }
        while (cur < n && intervals[cur][0] <= newInterval[1])
        {
            newInterval[0] = min(intervals[cur][0], newInterval[0]);
            newInterval[1] = max(intervals[cur][1], newInterval[1]);
            ++cur;
        }
        res.push_back(newInterval);
        while(cur < n) {
            res.push_back(intervals[cur++]);
        }

        return res;
    }
};
