/*
349的升级版，349只要求返回唯一的重复元素，350是只要intersection的部分重复的也需要给到
这里可以用 unodered_map 进行遍历 nums1 对于每一个 map[a] ++，后面对 nums2 遍历的时候 , if(map[a]-- > 0)(res.push_back(a)，因为如果只有1个话那肯定 -- 之后就 = 0 了
*/
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        // unordered_map 允许有重复元素
        unordered_map<int, int> m;
        vector<int> res;
        for(auto a : nums1) ++m[a];
        for(auto a : nums2) {
            if(--m[a] >= 0) res.push_back(a);
        }
        return res;
    }
};
