/*
intersecction of Two Arrays
把 nums1 放到 HashSet 中再遍历 nums2 有的话就加入到 res 最后返回 res
使用 unordered_set 正好保证了 element 的 unique
下面的就是时间复杂 O（N）的实现，只是需要额外的空间
*/

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> st(nums1.begin(), nums1.end()), res;
        for (auto a : nums2) {
            if (st.count(a)) res.insert(a);
        }
        return vector<int>(res.begin(), res.end());
    }
};
